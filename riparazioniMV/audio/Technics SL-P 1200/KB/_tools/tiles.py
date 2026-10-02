import cv2, numpy as np, json, os
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
out='/tmp/kb/KB/sheets'
S=[('S1_pcb_A','clean_p27-28.png','PCB sheet 1: FL(A), Operation(B), Spindle motor drive(C), Remote unit, Socket(F), Spindle control(G), Laser switch control(H), Pitch control(K), Pitch VR(L), Headphone amp(M), Extension; manual pp.49-51'),
   ('S2_pcb_B','clean_p29-30.png','PCB sheet 2: Main(D), Audio(I), Regulator(E), Line out(N), Power source(J); manual pp.52-54'),
   ('S3_sch_1','clean_p31-32.tif','Schematic 1 (grid cols 1-16): remote control unit, key codes, FL601 connections, Pitch control(K), Spindle motor drive(C), FL(A), Operation(B); manual pp.55-58'),
   ('S4_sch_2','clean_p33-34.tif','Schematic 2 (grid cols 17-34): Main P.C.B.(D) - system control, servo, DSP, RAM, filter; Regulator(E), Socket(F); manual pp.59-62'),
   ('S5_sch_3','clean_p35-36.tif','Schematic 3 (grid cols 35-53): Spindle control(G), Laser switch control(H), Audio(I) D/A, power source(J), Headphone(M), Line out(N); manual pp.63-66'),
   ('S6_block','clean_p37-38.tif','Block diagram; manual pp.67-70')]
T=1600; OV=200
meta={}
for name,f,desc in S:
    im=Image.open(f).convert('L')
    im=im.resize((im.width//2,im.height//2),Image.LANCZOS)   # 600->300 dpi
    W,H=im.size
    d=os.path.join(out,name); os.makedirs(d,exist_ok=True)
    im.save(os.path.join(d,'full_300dpi.png'),optimize=True)
    ov=im.resize((2000,int(H*2000/W)),Image.LANCZOS)
    ov.save(os.path.join(d,'overview.png'),optimize=True)
    tiles=[]
    xs=list(range(0,max(W-OV,1),T-OV)); ys=list(range(0,max(H-OV,1),T-OV))
    for r,y in enumerate(ys):
        for c,x in enumerate(xs):
            box=(x,y,min(x+T,W),min(y+T,H))
            tn='r%dc%d.png'%(r,c)
            im.crop(box).save(os.path.join(d,tn),optimize=True)
            tiles.append(dict(tile=tn,box=box))
    meta[name]=dict(src=f,desc=desc,size=[W,H],dpi=300,tiles=tiles,grid=[len(ys),len(xs)])
    print(name,W,H,len(ys),len(xs))
json.dump(meta,open('/tmp/kb/sheets_meta.json','w'),indent=1)
