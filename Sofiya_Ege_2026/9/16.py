l=[[int(d) for d in x.split()]for x in open('16.txt')]
ct=0
for x in l:
    x=sorted(x)
    povt = [d for d in x if x.count(d)>=2]
    nepovt = [d for d in x if x.count(d) == 1]
    if x[-1] in nepovt:
        if len(povt)>1:
            if x[-1]>3*((x[0]+x[1]+x[2]+x[3]+x[4]) / 5):
               ct+=1
print(ct)