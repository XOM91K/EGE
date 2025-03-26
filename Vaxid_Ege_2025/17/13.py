l = [int(x) for x in open('13.txt')]
sr = [d for d in l if str(d)[-1] == '7']
mx_sum = []
ct = 0
for x in range(len(l) - 1):
    if (l[x] < 0 and l[x + 1] > 0) or ( l[x] > 0 and l[x + 1] < 0):
        if l[x] + l[x + 1] < len(sr):
            ct = ct + 1
            mx_sum.append( l[x] + l[x + 1] )
print(ct, max(mx_sum))