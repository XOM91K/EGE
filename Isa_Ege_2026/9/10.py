l=[[int(d) for d in x.split()] for x in open('10.txt')]
ct=0
for x in l:
    povt3 = [d for d in x if x.count(d) >= 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3)>=3 and len(povt1)>=1:
        if (sum(povt3)/len(povt3)) > (sum(povt1)/len(povt1)):
            print(x)
            ct+=1
print(ct)