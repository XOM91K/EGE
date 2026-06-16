l = [int(x) for x in open('15.txt')]
s = []
mn = abs(min([x for x in l if str(x)[-2:] == '26']))
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 3:
        k += 1
    if len(str(abs(l[x + 1]))) == 3:
        k += 1
    if len(str(abs(l[x + 2]))) == 3:
        k += 1
    if k >= 1:
        if l[x] >= 0 and l[x + 1] >= 0 and l[x + 2] >= 0:
            if (l[x] + l[x + 1] + l[x + 2]) <= mn:
                s.append(l[x] + l[x + 1] + l[x + 2])
print(len(s), max(s))
