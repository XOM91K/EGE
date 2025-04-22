k=0
l = [sorted([int(d) for d in x.split()])for x in open("26.txt")]
for x in l:
    povt3 = [i for i in x if x.count(i) == 3]
    povt1 = [i for i in x if x.count(i) == 1]
    if len(povt3)==6 and len(povt1) == 1:
        if max(povt3) > povt1[0]:
            k+=1
print(k)