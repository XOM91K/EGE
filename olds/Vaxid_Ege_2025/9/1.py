l = [[int(d) for d in x.split()] for x in open('1.txt')]
# l = [x for x in range(1, 101) if x % 2 == 0 and x > 50]
ct = 0
for x in l:
    x.sort()
    if (x[0] + x[-1]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
        if len(set(x)) == 4:
            ct += 1
print(ct)