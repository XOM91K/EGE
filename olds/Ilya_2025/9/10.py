import math
l = [[int(d) for d in x.split()] for x in open('10.txt')]
ct = 0
k = 0
for x in l:
    k += 1
    can = True
    for y in range(len(x) - 1):
        if x[y] % 2 == x[y + 1] % 2:
            can = False
            break
    if can:
        povt = 1
        nepovt = []
        for y in x:
            if x.count(y) > 1:
                povt *= y
            else:
                nepovt.append(y)

        if sum(nepovt) * 3 >= povt:
            print(k, x)
            ct += k

print(ct)