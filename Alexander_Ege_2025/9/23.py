ct=0
l =[[int(d) for d in x.split()]for x in open("23.txt")]
for x in l:
    povt3 = [i for i in x if x.count(i) == 3]
    nepovt = [i for i in x if x.count(i) == 1]
    if len(povt3) == 3 and len(nepovt) == 3:
        if (sum(povt3))**2>(sum(nepovt))**2:
            ct+=1
print(ct,x)