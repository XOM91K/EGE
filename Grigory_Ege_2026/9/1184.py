l = [[int(d) for d in x.split()] for x in open('1184.txt')]
ct = 0
# [1, 1, 1, 2, 3, 4] len(set) => 4
# [1, 1, 2, 2, 3, 4] len(set) => 4
for x in l:
    povt3 = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt3) == 3 and len(nepovt) == 3:
        x = sorted(x)
        if x[-1] ** 2 + x[0] ** 2 >= (x[1] + x[2] + x[3] + x[4]) ** 2:
            ct += 1
print(ct)