import cv2, numpy as np, sys, json
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
cv2.setNumThreads(4)
S = 4  # downscale for matching

def load(p):
    return np.array(Image.open(p).convert('L'))

def estimate(A, B):
    a = cv2.resize(A, (A.shape[1]//S, A.shape[0]//S), interpolation=cv2.INTER_AREA)
    b = cv2.resize(B, (B.shape[1]//S, B.shape[0]//S), interpolation=cv2.INTER_AREA)
    det = cv2.SIFT_create(nfeatures=20000)
    ka, da = det.detectAndCompute(a, None)
    kb, db = det.detectAndCompute(b, None)
    m = cv2.BFMatcher(cv2.NORM_L2).knnMatch(db, da, k=2)
    good = [x[0] for x in m if len(x) == 2 and x[0].distance < 0.75 * x[1].distance]
    pb = np.float32([kb[g.queryIdx].pt for g in good])
    pa = np.float32([ka[g.trainIdx].pt for g in good])
    M, inl = cv2.estimateAffinePartial2D(pb, pa, method=cv2.RANSAC, ransacReprojThreshold=2.0, maxIters=20000, confidence=0.999)
    M[:, 2] *= S
    return M, int(inl.sum()), len(good)

def stitch(pa, pb, out):
    A = load(pa); B = load(pb)
    M, ninl, ng = estimate(A, B)
    h, w = B.shape
    corners = np.float32([[0,0],[w,0],[0,h],[w,h]])
    cb = cv2.transform(corners[None], M)[0]
    xs = np.concatenate([cb[:,0], [0, A.shape[1]]]); ys = np.concatenate([cb[:,1], [0, A.shape[0]]])
    x0, y0 = np.floor(xs.min()), np.floor(ys.min()); x1, y1 = np.ceil(xs.max()), np.ceil(ys.max())
    W, H = int(x1-x0), int(y1-y0)
    T = np.array([[1,0,-x0],[0,1,-y0]], np.float64)
    MB = M.copy(); MB[:,2] += [-x0, -y0]
    cA = cv2.warpAffine(A, T, (W, H), flags=cv2.INTER_NEAREST, borderValue=255)
    cB = cv2.warpAffine(B, MB, (W, H), flags=cv2.INTER_LINEAR, borderValue=255)
    # inside overlap use B only above seam, A below seam to avoid doubled lines
    # seam: middle of overlap in y (A starts at -y0 ; B ends at bottom of B)
    a_top = -y0; b_bot = cb[:,1].max() - y0
    seam = int((a_top + b_bot) / 2)
    C = cA.copy()
    C[:seam] = np.minimum(cA[:seam], cB[:seam])  # outside A this is just B
    C[:seam][cA[:seam] == 255] = cB[:seam][cA[:seam] == 255]
    C[:seam] = cB[:seam]
    C = np.where(C < 128, 0, 255).astype(np.uint8)
    C = np.rot90(C, k=-1)  # rotate clockwise -> upright text
    Image.fromarray(C).convert('1').save(out, compression='group4', dpi=(600, 600))
    ang = np.degrees(np.arctan2(M[1,0], M[0,0])); sc = np.hypot(M[0,0], M[1,0])
    return dict(out=out, inliers=ninl, matches=ng, dx=float(M[0,2]), dy=float(M[1,2]), angle=float(ang), scale=float(sc), size=C.shape[::-1], seam=seam)

if __name__ == '__main__':
    k = int(sys.argv[1])  # first page number
    r = stitch('full/i-%03d.png' % (k-27), 'full/i-%03d.png' % (k+1-27), 'sheet_p%d-%d.tif' % (k, k+1))
    print(json.dumps(r))
