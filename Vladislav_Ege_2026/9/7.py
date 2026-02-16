l = [[int(d) for d in x.split()] for x in open('7.txt')]
ct = 0
for x in l:
    x.sort()
    if (x[-1] + x[-2]) * 2 > 3 * (x[0] + x[1] + x[2]):
        c5 = [d for d in x if d % 10 == 5]
        if len(c5) >= 2:
            ct += 1
print(ct)