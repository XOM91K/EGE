l = [int(x) for x in open('26.txt')]
dv = sum([x for x in l if len(str(abs(x))) == 2 and x % 2 == 0])
mn = []
for x in range(len(l) - 1):
    k = 0
    if l[x] % dv == 0:
        k += 1
    if l[x + 1] % dv == 0:
        k += 1
    if k == 1:
        mn.append(l[x] * l[x + 1])
print(len(mn), abs(min(mn)))