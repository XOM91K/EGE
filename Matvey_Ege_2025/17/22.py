l = [int(x) for x in open('22.txt')]
mx4 = max([x for x in l if len(str(x)) == 4])
mn = []
for x in range(len(l) - 1):
    k = 0
    if l[x] <= mx4:
        k += 1
    if l[x + 1] <= mx4:
        k += 1
    if k == 1:
        if str(l[x] ** 2 + l[x + 1] ** 2)[-2:] == '12':
            mn.append(l[x] ** 2 + l[x + 1] ** 2)
print(len(mn), min(mn))