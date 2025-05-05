l = [int(x)for x in open('10.txt')]
mn = min([x for x in l if x % 2 == 0])
s = []
for x in range(len(l) - 2):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if k == 1:
        if l[x + 1] % mn == 0:
                s.append(l[x] + l[x + 2])
print(len(s), min(s))