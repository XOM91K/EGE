l = [int(x) for x in open('5.txt')]
itog = []
mn = min([x for x in l if str(x)[-2:] == '25'])
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k += 1
    if len(str(abs(l[x + 1]))) == 4:
        k += 1
    if len(str(abs(l[x + 2]))) == 4:
        k += 1
    if k >= 2:
        if l[x] * l[x + 1] * l[x + 2] <= mn ** 2:
            itog.append(l[x] * l[x + 1] * l[x + 2])
print(len(itog), max(itog))