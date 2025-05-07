l = [int(x) for x in open('18.txt')]
sr = [d for d in l if str(d)[-3:] == '151']
sr = sum(sr) / len(sr)
mn_sum = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4:
        k = k + 1
    if len(str(abs(l[x + 1]))) == 4:
        k = k + 1
    if len(str(abs(l[x + 2]))) == 4:
        k = k + 1
    if 1 <= k <= 2:
        k = 0
        g = 0
        if l[x] % 13 == 0:
            k = k + 1
        if l[x + 1] % 13 == 0:
            k = k + 1
        if l[x + 2] % 13 == 0:
            k = k + 1
        if l[x] % 7 == 0:
            g = g + 1
        if l[x + 1] % 7 == 0:
            g = g + 1
        if l[x + 2] % 7 == 0:
            g = g + 1
        if k > g:
            if l[x] > sr and l[x + 1] > sr and l[x + 2] > sr:
                ct = ct + 1
                mn_sum.append( l[x] + l[x + 1] + l[x + 2] )
print(ct, min(mn_sum))