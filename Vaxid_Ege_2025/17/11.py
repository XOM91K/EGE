l = [int(x) for x in open('11.txt')]
mx = max([d for d in l if str(d)[-1] == '1'])
mn_sum = []
ct = 0
for x in range(len(l) - 3):
    if (l[x] % 2 + l[x + 1] % 2 + l[x + 2] % 2 + l[x + 3] % 2) % 2 != 0:
        if l[x] < mx and l[x + 1] < mx and l[x + 2] < mx and l[x + 3] < mx:
            ct = ct + 1
            mn_sum.append( l[x] + l[x + 1] + l[x + 2] + l[x + 3] )
print(ct, min(mn_sum))