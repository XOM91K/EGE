l=[[int(d) for d in x.split()] for x in open('6.txt')]
ct=0
for x in l:
    x=sorted(x)
    if x.count(x[0])==1 and len(set(x)) < 6:
        print(x)
        if x[0]+x[-1]<((x[1]+x[2]+x[3]+x[4])/4)*2:
            ct+=1
print(ct)