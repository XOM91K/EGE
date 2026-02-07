l = [[int(d) for d in x.split()] for x in open('3.txt')]
ct = 0
for x in l:
    povt2 = [d for d in x if x.count(d) == 2]
    if len(povt2) == 2:
        x = sorted(x)
        if x[2] + x[3] > (x[0] + x[1]) * 2:
            if x[3] % x[0] != 0:
                ct += 1
print(ct)