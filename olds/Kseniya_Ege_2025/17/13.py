l = [int(x) for x in open('13.txt')]
mn2 = min([x for x in l if len(str(abs(x))) == 2])
print(mn2)
mx4 = max([x for x in l if len(str(abs(x))) == 4 and str(x)[-1] == '1'])
print(mx4)
sm = []
for x in range(len(l) - 2):
    k = 0
    if l[x] > mn2 ** 2:
        k += 1
    if l[x + 1] > mn2 ** 2:
        k += 1
    if l[x + 2] > mn2 ** 2:
        k += 1
    if k == 2:
        if (abs(l[x]) * abs(l[x + 1]) * abs(l[x + 2])) % mx4 == 0:
            sm.append(abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]))
print(len(sm), max(sm))