l=[[int(d) for d in x.split()] for x in open(r'C:\Users\Zarif\Desktop\1547_1 (4).csv')]
sm = 0
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    povt2 = [d for d in x if x.count(d) == 2]
    povt3 = [d for d in x if x.count(d) == 3]
    if x[0] >= x[1] >= x[2] >= x[3] >= x[4] >= x[5]:
        if len(povt1) == 1 and len(povt3) == 3 and len(povt2) == 2:
            if min(povt2 + povt3) > povt1[0]:
                sm += sum(x)
print(sm)