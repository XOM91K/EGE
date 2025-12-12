f=open('11.txt')
ct=0
for s in f:
    a=[int(x) for x in s.split()]
    povt2=[x for x in a if a.count(x)==2]
    nepovt=[x for x in a if a.count(x)==1]
    if len(nepovt) > 0:
        if len(povt2)==2 and len(nepovt) == 4 and (sum(nepovt)/len(nepovt))<=sum(povt2):
            ct+=1
print(ct)