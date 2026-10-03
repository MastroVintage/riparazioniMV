import json
m={}
def put(prefix,nums):
    for i,n in enumerate(nums):
        if n is not None: m['%s-%03d'%(prefix,i)]=n
put('scan0056',[30,29,28,27,25,26,24,23,21,22,20,19,17,18,16,15,13,14,12,11,9,10,8,7,5,6,4,3,1,2,None,None])
put('scan0057',[50,49,47,48,46,45,43,44,42,41,39,40,38,37,35,36,34,33])
put('scan0058',[32,31,70,69,67,68,66,65,63,64,62,61,59,60,58,57,55,56,54,53,51,52])
put('scan0059',[72,71,73,74,76,75,77,78,80,79,81,82,84,83,85,86])
put('scan0060',[87,88,90,89,91,92,94,93])
put('scan0061',[None]*8+[96,95,98,97,99,100,102,101,103,104,106,105,107,108,110,109])
put('scan0062',[111,112,113,114,116,115,117,118,120,119,121,122,124,123,125,126,128,127,129,130])
put('scan0063',[132,131,133,134,136,135,137,138,140,139,141,None])
v=sorted(m.values()); assert v==list(range(1,142)), [n for n in range(1,142) if n not in v]
extra={'scan0056-031':-2,'scan0056-030':-1,'scan0063-011':999}
order=sorted(list(m.items())+list(extra.items()),key=lambda x:x[1])
json.dump(order,open('order.json','w')); print(len(order))
