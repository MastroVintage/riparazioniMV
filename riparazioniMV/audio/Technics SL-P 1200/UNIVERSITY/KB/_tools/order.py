import json
m={}
A={0:7,1:8,2:5,3:6,4:3,5:4,6:1,7:2}
for k,v in A.items(): m['A-%03d'%k]=v
for i in range(20): m['B-%03d'%i]=(27,28,25,26,23,24,21,22,19,20,17,18,15,16,13,14,11,12,9,10)[i]
for i in range(20): m['C-%03d'%i]=(47,48,45,46,43,44,41,42,39,40,37,38,35,36,33,34,31,32,29,30)[i]
D=(66,67,64,65,62,63,60,61,58,59,56,57,None,55,53,54,51,52,49,50)
for i in range(20):
    if D[i]: m['D-%03d'%i]=D[i]
E=(86,None,84,85,82,83,80,81,78,79,76,77,74,75,72,73,70,71,68,69)
for i in range(20):
    if E[i]: m['E-%03d'%i]=E[i]
# unnumbered: sort key
un={'A-011':-3,'A-010':-2,'A-008':-1,'A-009':0.5,'D-012':54.5,'E-001':86.5}
nums=sorted(m.values()); assert nums==list(range(1,87)),[n for n in range(1,87) if n not in nums]
order=sorted(list(m.items())+list(un.items()),key=lambda x:x[1])
json.dump(order,open('order.json','w'))
print(len(order)); print(order[:12])
