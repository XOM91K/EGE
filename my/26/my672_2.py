l = sorted([int(x) for x in open('my672.txt')])
D = 3000
E = 1000
ct = 0
lstD = lstE = 0
for x in range(len(l) - 1):
    if l[x] > 500:
        if D - l[x] - l[x + 1] >= 0:
            D -= l[x]
            ct += 1
        elif D - l[x] >= 0:
            lstD = l[x]
            ct += 1
    else:
        if E - l[x] - l[x + 1] >= 0:
            E -= l[x]
            ct += 1
        elif E - l[x] >= 0:
            lstE = l[x]
            ct += 1
print(ct, lstE, lstD)
