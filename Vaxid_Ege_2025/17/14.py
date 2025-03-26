l = [int(x) for x in open('14.txt')]
mx = max([d for d in l if str(d)[-1] == '7'])
mx_sum = []
ct = 0
for x in range(len(l) - 1):
    if str(l[x])[0] == str(l[x + 1])[0]:
        k = 0
        if str(l[x])[-1] == '7' and len(str(l[x])) == 3:
            k = k + 1
        if str(l[x + 1]) == '7' and len(str(l[x + 1])) == 3:
            k = k + 1
        if k >= 1:
            if l[x] + l[x + 1] < mx:
                ct = ct + 1
                mx_sum.append( l[x] + l[x + 1] )
print(ct, max(mx_sum))