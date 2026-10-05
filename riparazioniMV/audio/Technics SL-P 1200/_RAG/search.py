"""Ricerca BM25 sul corpus (senza dipendenze).  python _RAG/search.py "AN8370S focus search" [-k 8] [-s TG_SL-P150]"""
import json, math, re, sys, os, collections
here=os.path.dirname(os.path.abspath(__file__))
args=sys.argv[1:]; k=8; src=None
if '-k' in args: i=args.index('-k'); k=int(args[i+1]); del args[i:i+2]
if '-s' in args: i=args.index('-s'); src=args[i+1]; del args[i:i+2]
q=' '.join(args)
tok=lambda s:re.findall(r'[a-z0-9]+',s.lower())
docs=[json.loads(l) for l in open(os.path.join(here,'corpus.jsonl'),encoding='utf-8')]
if src: docs=[d for d in docs if d['source']==src]
toks=[tok(d['text']+' '+d['section']+' '+' '.join(d['chips'])) for d in docs]
N=len(docs); avg=sum(map(len,toks))/max(N,1); df=collections.Counter(t for ts in toks for t in set(ts))
qt=tok(q); sc=[]
for d,ts in zip(docs,toks):
    tf=collections.Counter(ts); s=0
    for t in qt:
        if t in tf: s+=math.log(1+(N-df[t]+.5)/(df[t]+.5))*tf[t]*2.2/(tf[t]+1.2*(.25+.75*len(ts)/avg))
    sc.append(s)
for s,d in sorted(zip(sc,docs),key=lambda x:-x[0])[:k]:
    if s<=0: break
    print('%.1f  %s  p.%s  [%s]  %s'%(s,d['source'],d['page'],d['section'][:60],d['image']))
    print('     '+d['text'][:240].replace('\n',' | '))
