l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    x.sort()
    if (max(x) + min(x)) ** 2 > x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
        print(x)
        ct += 1
print(ct)