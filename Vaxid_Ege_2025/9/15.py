l = [sorted([int(d) for d in x.split()]) for x in open('15.txt')]
ct = 0
for x in l:
    if 2 * (x[3] + x[4]) > 3 * (x[0] + x[1] + x[2]):
        ok = [y for y in x if str(y)[-1] == '5']
        if len(ok) >= 2:
            ct = ct + 1
print(ct)
