l = [int(x) for x in open( '9.txt' )]
mn = min([d for d in l if d % 2 == 0])
mn_sum = []
ct = 0
for x in range(len(l) - 2):
    if (l[x] % 2 == 0 and l[x+2] % 2 != 0) or (l[x] % 2 != 0 and l[x+2] % 2 == 0):
        if l[x + 1] % mn == 0:
            ct = ct + 1
            mn_sum.append(l[x] + l[x+2])
print(ct, min(mn_sum))