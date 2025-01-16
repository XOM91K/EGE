l = [int(x) for x in open('22.txt')]
ct = 0
mn = []
mx43 = max([x for x in l if abs(x) % 100 == 43 and len(str(abs(x))) == 5])
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and abs(l[x]) % 100 == 43:
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and abs(l[x + 1]) % 100 == 43:
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and abs(l[x + 2]) % 100 == 43:
        k += 1
    if k >= 1:
        if l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 <= mx43 ** 2:
            ct += 1
            mn.append(l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2)
print(ct, min(mn))