l = sorted([int(x) for x in open('1.txt')])
ct = 0
print(l)
for x in range(len(l) - 2):
    if l[x + 2] < l[x] + l[x + 1]:
        ct += 1
print(ct)