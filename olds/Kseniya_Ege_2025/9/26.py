l = [[int(d) for d in x.split()] for x in open('26.txt')]
ct = 0
for x in l:
    # [22, 22, 22, 1, 2, 3] = len(set(x) = 4
    # [22, 22, 44, 44, 1, 2] = len(set(x)) = 4
    povt3 = [y for y in x if x.count(y) == 3]
    nepovt = [y for y in x if x.count(y) == 1]
    if len(povt3) == 3 and len(nepovt) == 3:
        x.sort()
        if x[-1] ** 2 + x[0] ** 2 >= (x[1] + x[2] + x[3] + x[4]) ** 2:
            ct += 1
print(ct)