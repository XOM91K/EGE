l = [int(x) for x in open('27.txt')]
mx = []
mx2 = max([x for x in l if str(x)[-2:] == '25' and len(str(abs(x))) == 5])
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and str(l[x])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2])[-2:] == '25':
        k += 1
    if k > 0:
        if l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 <= mx2 ** 2:
            mx.append(l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 )
print(len(mx), min(mx))