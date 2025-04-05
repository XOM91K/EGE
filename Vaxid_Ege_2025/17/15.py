l = [int(x) for x in open('15.txt')]
sr = [d for d in l if d % 32 == 0]
print(-132 )
mx_sum = []
ct = 0
for x in range(len(l) - 1):
    k = 0
    if l[x] < 0:
        k = k + 1
    if l[x + 1] < 0:
        k = k + 1
    if k >= 1:
        if ( l[x] + l[x + 1] ) < len(sr):
            ct = ct + 1
            mx_sum.append( l[x] + l[x + 1] )
print(ct, max(mx_sum))