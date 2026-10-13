"""Pulizia scansioni grigie/colore (skill acquisizione-documenti-tecnici, punto 5).
uso: python clean_gray.py in.png out.png"""
import sys, numpy as np, cv2
def deskew(g):
    s=cv2.resize(255-g,None,fx=0.25,fy=0.25); best=(0,-1)
    for a in np.arange(-2,2.01,0.1):
        M=cv2.getRotationMatrix2D((s.shape[1]/2,s.shape[0]/2),a,1)
        r=cv2.warpAffine(s,M,(s.shape[1],s.shape[0])); v=r.sum(1).astype(float).var()
        if v>best[1]: best=(a,v)
    a=best[0]
    if abs(a)<0.05: return g,0.0
    M=cv2.getRotationMatrix2D((g.shape[1]/2,g.shape[0]/2),a,1)
    return cv2.warpAffine(g,M,(g.shape[1],g.shape[0]),flags=cv2.INTER_CUBIC,borderValue=255),a
def clean(src,dst):
    g=cv2.imread(src,cv2.IMREAD_GRAYSCALE); h,w=g.shape
    bg=cv2.morphologyEx(g,cv2.MORPH_CLOSE,np.ones((41,41),np.uint8))
    n=np.clip(g.astype(float)/np.maximum(bg,1)*255,0,255)
    lo,hi=95,185; n=np.clip((n-lo)/(hi-lo),0,1)**1.3*255
    n=n.astype(np.uint8)
    mx,my=int(w*0.004),int(h*0.015)
    n[:, :mx]=255; n[:, w-mx:]=255; n[:my,:]=255; n[h-my:,:]=255
    # fori/ombre ai lati: componenti interamente nella fascia esterna 4.5%
    band=int(w*0.045); ink=(n<160).astype(np.uint8)
    k,lab,st,_=cv2.connectedComponentsWithStats(ink,8)
    for i in range(1,k):
        x,y,bw,bh,a=st[i]
        blob=40<=bw<=220 and 40<=bh<=260 and 0.5<bw/bh<2 and a>0.35*bw*bh  # foro/ombra tondeggiante
        edge=(x<=2 or x+bw>=w-2) and a>0.3*bw*bh                            # ombra del bordo carta
        if (x+bw<=band or x>=w-band) and (blob or edge): n[lab==i]=255
    n,a=deskew(n)
    n=(np.round(n/17)*17).astype(np.uint8)
    cv2.imwrite(dst,n,[cv2.IMWRITE_PNG_COMPRESSION,9]); return a
if __name__=='__main__': print(sys.argv[1], 'deskew', clean(sys.argv[1],sys.argv[2]))
