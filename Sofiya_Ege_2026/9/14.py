import math
l=[[int(d) for d in x.split(':')]for x in open('992_1 (8).csv')]
ct=0
for x in l:
    x=sorted(x)
    povt = [d for d in x if x.count(d)>=2]
    nepovt = [d for d in x if x.count(d) == 1]
    if len(povt)>1:
        if 3*sum(nepovt)<=math.prod(povt):
               ct+=1
print(ct)