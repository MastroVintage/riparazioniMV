from PIL import Image
import glob,os,json,subprocess
rot={}
for f in glob.glob('osd/*.txt'):
    t=open(f).read().split()
    r=int(t[1]) if len(t)>1 else 0
    rot[os.path.basename(f)[:-4]]=r
json.dump(rot,open('rot.json','w'))
for b,r in rot.items():
    im=Image.open('raw/%s.jpg'%b).convert('L')
    if r in (180,270): im=im.rotate(180)
    im.save('norm/%s.png'%b)
    w,h=im.size
    im.crop((0,int(h*0.90),w,h)).save('/tmp/uni/foot_%s.png'%b)
