par = []
ct = 0
l = [int(x) for x in open('8.txt')]
srar = sum(l) / len(l)
for x in range(1, len(l) - 2):
    if (l[x] * l[x + 1]) > l[x - 1] * l[x + 2]:
        par.append(l[x] + l[x + 1])
        if l[x] > srar or l[x + 1] > srar:
            ct += 1
print(ct)
print(max(par))