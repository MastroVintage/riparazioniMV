"""Costruisce _RAG/corpus.jsonl da tutte le KB del progetto SL-P1200.
Eseguire dalla cartella 'Technics SL-P 1200':  python _RAG/build_corpus.py"""
import os, re, json, glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=[ # id, titolo, cartella KB (relativa), tipo, rilevanza
 ('SM_SL-P1200','Technics SL-P1200 Service Manual (HAD8609723C0)','KB','service_manual','dispositivo'),
 ('TG17_SL-XP7','Technical Guide Vol.17 SL-XP7 (APD860582)','UNIVERSITY/KB','training','media'),
 ('TG_SL-P150','Technical Guide CD Player Technology SL-P150/SL-P405C (AD8812333T0)','UNIVERSITY/TG_SL-P150_CD_Player_Technology/KB','training','alta'),
 ('TG25_AutoCD','Technical Guide Vol.25 Auto CD Technology','UNIVERSITY/A_TG_Vol25_Auto_CD_Technology/KB','training','alta (Type C)'),
 ('TSG_1986-1990','Troubleshooting Guide CD Players 1986-1990 (MSC910101)','UNIVERSITY/B_Troubleshooting_Guide_1986-1990/KB','training','alta'),
 ('TG_Adjustments','Technical Guide Purposes of CD Adjustments One-Beam (AD8806133G0)','UNIVERSITY/C_TG_Purposes_of_Adjustments_OneBeam/KB','training','alta'),
]
# Articoli di riparazione: rilevati automaticamente (ARTICOLI_RIPARAZIONI/<id>/KB)
for _kb in sorted(glob.glob(os.path.join(ROOT,'ARTICOLI_RIPARAZIONI','*','KB'))):
    _id=os.path.basename(os.path.dirname(_kb)); _t=_id
    _ix=os.path.join(_kb,'00_INDEX.md')
    if os.path.exists(_ix):
        for _l in open(_ix,encoding='utf-8',errors='ignore'):
            if _l.startswith('#'): _t=_l.lstrip('# ').strip(); break
    SRC.append((_id,_t,os.path.relpath(_kb,ROOT).replace('\\','/'),'article','vedi 00_INDEX'))
# Service manual di altri modelli Technics: rilevati automaticamente (SERVICE_MANUALS_CORRELATI/<modello>/KB, struttura come KB del dispositivo)
for _kb in sorted(glob.glob(os.path.join(ROOT,'SERVICE_MANUALS_CORRELATI','*','KB'))):
    _id='SM_'+os.path.basename(os.path.dirname(_kb)); _t=_id
    _ix=os.path.join(_kb,'00_INDEX.md')
    if os.path.exists(_ix):
        for _l in open(_ix,encoding='utf-8',errors='ignore'):
            if _l.startswith('#'): _t=_l.lstrip('# ').strip(); break
    SRC.append((_id,_t,os.path.relpath(_kb,ROOT).replace('\\','/'),'service_manual_related','vedi 00_INDEX'))
CHIP=re.compile(r'\b((?:AN|MN|PCM|NJM|EHDGA)\d{3,5}[A-Z]{0,4}(?:-\d+)?)\b')
REF=re.compile(r'\b((?:IC|TJ|VR|CN|TP|Q|D)\s?\d{1,4})\b')
def topics(kb):
    f=os.path.join(kb,'topics.tsv'); out=[]
    if not os.path.exists(f): return out
    for l in open(f,encoding='utf-8'):
        p=l.rstrip('\n').split('\t')
        if len(p)<3 or l.startswith(('#','section')): continue
        m=re.match(r'(\d+)(?:-(\d+))?',p[2].strip())
        if m: out.append((int(m.group(1)),int(m.group(2) or m.group(1)),p[0]+' '+p[1][:90]))
    return out
def clean(t):
    keep=[]
    for line in t.splitlines():
        s=line.strip()
        if len(s)<2: continue
        al=sum(c.isalnum() for c in s)/len(s)
        if al<0.5 and len(s)<40: continue
        keep.append(s)
    return re.sub(r'[ \t]+',' ','\n'.join(keep))
def chunks(t,n=1400,ov=200):
    if len(t)<=n: return [t]
    out=[];i=0
    while i<len(t):
        j=min(len(t),i+n)
        if j<len(t):
            k=t.rfind('\n',i+n//2,j)
            if k>0: j=k
        out.append(t[i:j]); 
        if j>=len(t): break
        i=max(j-ov,i+1)
    return out
recs=[]
for sid,title,kbrel,kind,rel in SRC:
    kb=os.path.join(ROOT,kbrel)
    if not os.path.isdir(kb): continue
    if sid=='SM_SL-P1200' or kind=='service_manual_related': ocrd=os.path.join(kb,'manual','ocr'); imgd=kbrel+'/manual/img'
    else: ocrd=os.path.join(kb,'ocr'); imgd=kbrel+'/pages'
    tp=topics(kb)
    files=sorted(glob.glob(os.path.join(ocrd,'*.txt')))
    if kind=='article':  # scheda + eventuale testo nativo
        files=[os.path.join(kb,n) for n in ('00_INDEX.md','testo.md') if os.path.exists(os.path.join(kb,n))]+files
    for f in files:
        tag=os.path.splitext(os.path.basename(f))[0]
        m=re.match(r'[pm](\d+)',tag); page=int(m.group(1)) if m and not tag.startswith(('p000','m00','p999')) else None
        sec=next((s for a,b,s in tp if page is not None and a<=page<=b),'')
        txt=clean(open(f,encoding='utf-8',errors='ignore').read())
        if len(txt)<30: continue
        for k,c in enumerate(chunks(txt)):
            recs.append(dict(id='%s:%s:%d'%(sid,tag,k),source=sid,title=title,kind=kind,relevance_SL_P1200=rel,
              page=page,page_tag=tag,section=sec,chips=sorted(set(CHIP.findall(c))),refs=sorted(set(r.replace(' ','') for r in REF.findall(c)))[:40],
              image=imgd+'/'+tag+'.png',text=c))
os.makedirs(os.path.join(ROOT,'_RAG'),exist_ok=True)
with open(os.path.join(ROOT,'_RAG','corpus.jsonl'),'w',encoding='utf-8') as fo:
    for r in recs: fo.write(json.dumps(r,ensure_ascii=False)+'\n')
print(len(recs),'chunk')
