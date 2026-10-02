import cv2, numpy as np, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
k=int(sys.argv[1]); mode=sys.argv[2]
im=np.array(Image.open('sheet_p%d-%d.tif'%(k,k+1)).convert('L'))
ink=(im<128).astype(np.uint8)
if mode=='pcb':
    inkf=ink.astype(np.float32)
    d=cv2.GaussianBlur(inkf,(0,0),2.2)
    d2=cv2.GaussianBlur(inkf,(0,0),4)
    w,b=0.07,0.40
    t=np.clip((d2-w)/(b-w),0,1)
    out=np.where(d>0.42,0,255-t*190)
    out=(np.round(out/17)*17).clip(0,255).astype(np.uint8)
    Image.fromarray(out).save('clean_p%d-%d.png'%(k,k+1),compress_level=9)
else:
    n,lab,st,_=cv2.connectedComponentsWithStats(ink,connectivity=8)
    small=st[:,cv2.CC_STAT_AREA]<=12; small[0]=False
    sm=small[lab].astype(np.uint8); del lab
    big=ink&(1-sm)
    near=cv2.dilate(big,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17)))
    # also keep small dots that cluster together (halftone fills)
    dens=cv2.blur(sm.astype(np.float32),(15,15))
    lone=(sm==1)&(near==0)&(dens<0.03)
    ink[lone]=0
    print('removed px',int(lone.sum()))
    Image.fromarray(((1-ink)*255).astype(np.uint8)).convert('1').save('clean_p%d-%d.tif'%(k,k+1),compression='group4',dpi=(600,600))
