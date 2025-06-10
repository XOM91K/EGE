l = [int(x) for x in open('6.txt')]
ct = 0
c = []
chisla = [y for y in l if str(y)[-1] == '7']
mx = max(chisla)
for i in range(len(l) - 2):
    ct1 = 0
    ctx = 0
    if l[i]%2 != 0:
        ct1 += 1
    if l[i+1] % 2 != 0:
        ct1 += 1
    if l[i+2]%2 != 0:
        ct1 += 1
    if ct1 == 2:
        if l[i] > mx:
            ctx += 1
        if l[i + 1] > mx:
            ctx += 1
        if l[i + 2] > mx:
            ctx += 1
        if ctx == 1:
            ct += 1
            c.append(l[i])
            c.append(l[i + 1])
            c.append(l[i + 2])
d = sum(set(c)) / len(set(c))
print(ct, d)