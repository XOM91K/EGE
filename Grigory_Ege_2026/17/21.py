l = [int(d) for d in open('21.txt')]
A = []
ct = 0
mx = max([y for y in l if str(abs(y))[:2] == '45'])
for x in range(len(l) - 2):
    k = 0
    if l[x] < 0:
        k += 1
    if l[x + 1] < 0:
        k += 1
    if l[x + 2] < 0:
        k += 1
    if k == 1:
        if l[x] + l[x + 1] + l[x + 2] >= mx:
            ct += 1
            if str(l[x] + l[x + 1] + l[x + 2])[-2:] == '45':
                A.append(l[x] + l[x + 1] + l[x + 2])
print(ct, min(A))
