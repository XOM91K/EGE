l = [sorted([int(y) for y in x.split()]) for x in open('1.txt')]
ct = 0
for x in l:
    if x[-1] ** 2 == x[0] ** 2 + x[1] ** 2:
        ct += 1
print(ct)