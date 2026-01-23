l = [int(x) for x in open('16.txt')]
mxl = max([y for y in l if len(str(abs(y))) == 5 and str(abs(y))[-2:] == '25']) ** 2
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and str(l[x])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2])[-2:] == '25':
        k += 1
    if k >= 1:
        if l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 <= mxl:
            mn.append(l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2)
print(len(mn), min(mn))

