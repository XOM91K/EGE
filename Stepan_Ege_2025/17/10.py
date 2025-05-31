l = [int(x) for x in open('10.txt')]
mx = []
mxpt = max([y for y in l if len(str(abs(y))) == 5 and str(y)[-2:] == '25']) ** 2
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and str(l[x])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2])[-2:] == '25':
        k += 1
    if k > 0:
        if (l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2) <= mxpt:
            mx.append(l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2)
print(len(mx), min(mx))