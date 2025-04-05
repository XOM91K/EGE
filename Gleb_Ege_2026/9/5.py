l = [[int(d) for d in x.split()] for x in open('5.txt')]
sm = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt2 = [d for d in x if x.count(d) == 2]
    if len(povt3) == 3 and len(povt2) == 4:
        x.sort()
        ct_nch = [d for d in x[:4] if d % 2 != 0]
        if len(ct_nch) == 2:
            sm += sum(x)
print(sm)