l = [int(x) for x in open('11.txt')]
dv = sum([y for y in l if y % 2 == 0 and len(str(abs(y))) == 2])
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