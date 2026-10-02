import cv2, numpy as np, json, sys
from PIL import Image
order=json.load(open('order.json')); rot=json.load(open('rot.json'))
order=[o for o in order if o[0]!='E-001']
def deskew(g):
    s=cv2.resize(g,(g.shape[1]//4,g.shape[0]//4),interpolation=cv2.INTER_AREA)
    b=(s<140).astype(np.float32)
    best=(0,-1)
    h,w=b.shape
    for a in np.arange(-2.0,2.01,0.1):
        M=cv2.getRotationMatrix2D((w/2,h/2),a,1)
        r=cv2.warpAffine(b,M,(w,h))
        v=np.var(r.sum(1))
        if v>best[1]: best=(a,v)
    return best[0]
def clean(b):
    g=np.array(Image.open('norm/%s.png'%b).convert('L'))
    H,W=g.shape
    # whiten margins (punch holes, scanner edges)
    mx,my=int(W*0.055),int(H*0.025)
    g[:, :mx]=255; g[:, W-mx:]=255; g[:my,:]=255; g[H-my:,:]=255
    if rot[b] in (90,270): g=np.rot90(g,k=-1).copy()   # content upright (clockwise 90)
    a=deskew(g)
    H,W=g.shape
    M=cv2.getRotationMatrix2D((W/2,H/2),a,1)
    g=cv2.warpAffine(g,M,(W,H),flags=cv2.INTER_LINEAR,borderValue=255)
    # background normalisation
    bg=cv2.morphologyEx(g,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_RECT,(41,41)))
    n=np.clip(g.astype(np.float32)/np.maximum(bg,1)*255,0,255)
    # levels: remove show-through (light) keep dark
    lo,hi=95,185
    o=np.clip((n-lo)/(hi-lo),0,1)
    o=(o**1.3)*255
    o=(np.round(o/17)*17).astype(np.uint8)
    return o,a
if __name__=='__main__':
    import os; os.makedirs('clean',exist_ok=True)
    log=[]
    for b,p in order[int(sys.argv[1]):int(sys.argv[2])]:
        o,a=clean(b)
        tag='p%03d'%p if p==int(p) and p>0 else {'A-011':'p000a_cover','A-010':'p000b_contents1','A-008':'p000c_contents2','A-009':'p000d_divider_circuit_operation','D-012':'p054b_divider_troubleshooting'}[b]
        Image.fromarray(o).save('clean/%s.png'%tag,compress_level=9)
        log.append((tag,b,round(float(a),2)))
    print(log)
