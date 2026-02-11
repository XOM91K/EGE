l = [[int(d) for d in x.split()] for x in open('5.txt')]
ct = 0
for x in l:
    x = sorted(x)
    if (x[3] + x[4]) * 2 > (x[0] + x[1] + x[2]) * 3:
        fv = [d for d in x if str(d)[-1] == '5']
        if len(fv) >= 2:
            ct += 1
print(ct)