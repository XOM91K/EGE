l = [int(d) for d in open('14.txt')]
ZOV = []
m = max(l)
for x in range(len(l) - 2):
    k = 0
    if '0' not in str(l[x]):
        k += 1
    if '0' not in str(l[x + 1]):
        k += 1
    if '0' not in str(l[x + 2]):
        k += 1
    if k >= 2:
        if l[x] + l[x + 1] + l[x + 2] < m / 2:
            ZOV.append(l[x] + l[x + 1] + l[x + 2])
print(len(ZOV), max(ZOV))
