l=[[int(d) for d in x.split()]for x in open('22.txt')]
ct=0
for x in l:
    povt3=[a for a in x if x.count(a)>=3]
    nepovt = [a for a in x if x.count(a) ==1]
    povt = [a for a in x if x.count(a) >1]
    if len(set(povt3))==1 and len(nepovt)>=1 and sum(povt)/len(povt)<sum(nepovt) / len(nepovt):
        ct+=1
print(ct)