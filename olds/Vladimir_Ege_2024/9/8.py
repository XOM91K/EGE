l = [sorted([int(d) for d in x.split()]) for x in open('8.txt')]
ct = 0
for x in l:
    if (x[-1] + x[0]) % 3 == 0:
        if x[1] - x[0] == x[-1] - x[-2]:
            ct += 1
print(ct)