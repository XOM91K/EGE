l = [[int(d) for d in x.split()] for x in open('4.txt')]
ct = 0
for x in l:
    x.sort()
    if x[4] ** 2 > x[0] * x[1] * x[2] * x[3]:
        if x[3] + x[4] > (x[0] + x[1] + x[2]) * 2:
            ct += 1
print(ct)