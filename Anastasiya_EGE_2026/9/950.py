l=[[int(d) for d in x.split()] for x in open('950.txt')]
ct=0
for x in l:
    povt=[y for y in x if x.count(y)>1]
    if len(povt)>0:
        if x.count(max(x))==1:
            if (max(x)/((sum(x)-max(x))/5))>3:
                ct+=1
print(ct)