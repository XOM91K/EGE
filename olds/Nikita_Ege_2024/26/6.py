l = [[int(d) for d in x.split()] for x in open('6.txt')]
l = sorted(l, key=lambda d: d[1])
time_k = 0
ct = 0
tm_k = []
for x in l:
    if x[0] - time_k >= 10:
        time_k = x[1]
        tm_k.append([x[0], x[1]])
        ct += 1
mx_rzn = 0
for x in l:
    if x[0] - tm_k[-2][1] >= 10:
        mx_rzn = max(mx_rzn, x[0] - tm_k[-2][1])
print(ct, mx_rzn)