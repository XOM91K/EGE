l = [int(x) for x in open('9.txt')]
mx69 = max([d for d in l if str(d)[-2:] == '69']) ** 2
pol17 = sorted([d for d in l if d > 0 and d % 17 == 0])
smmn = pol17[0] + pol17[1]
mn = []
for x in range(len(l) - 3):
    k = 0
    if len(str(abs(l[x]))) == 3:
        k += 1
    if len(str(abs(l[x + 1]))) == 3:
        k += 1
    if len(str(abs(l[x + 2]))) == 3:
        k += 1
    if len(str(abs(l[x + 3]))) == 3:
        k += 1
    if k == 2:
        k = 0
        if l[x] % 18 == 0:
            k += 1
        if l[x + 1] % 18 == 0:
            k += 1
        if l[x + 2] % 18 == 0:
            k += 1
        if l[x + 3] % 18 == 0:
            k += 1
        if k == 1:
            if (l[x] + l[x + 1] + l[x + 2] + l[x + 3]) % smmn == 0:
                if (l[x] * l[x + 1] * l[x + 2] * l[x + 3]) <= mx69:
                    mn.append((l[x] + l[x + 1] + l[x + 2] + l[x + 3]) ** 2)

print(len(mn), min(mn))