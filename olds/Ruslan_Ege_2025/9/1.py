l = [sorted([int(d) for d in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if len(set(x)) == 4:
        if (x[0] + x[-1]) ** 2 < x[1] ** 2 + x[2] ** 2 + x[3] ** 2:
            ct += 1
print(ct)
# l = [22, 11, 19, -5, -3, -2]
# r = [x for x in l if x % 2 != 0 and x > 5]
# print(r)