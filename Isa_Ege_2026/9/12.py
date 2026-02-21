l=[[int(d) for d in x.split()] for x in open('12.txt')]
k=0
for x in l:
    k += 1
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 6 and len(povt1) == 1:
        if sum(povt3) / 6 < povt1[0]:
            print(k)