l = [int(x) for x in open('6.txt')]
mx = 0
for x in l:
    if str(x)[-2:] == '15':
        mx = max(mx, x)
ct = 0
mx_tr = 0
for x in range(len(l) - 2):
    r = [len(str(l[x])), len(str(l[x + 1])), len(str(l[x + 2]))]
    if r.count(4) == 1 and l[x] + l[x + 1] + l[x + 2] >= mx:
        ct += 1
        mx_tr = max(mx_tr, l[x] + l[x + 1] + l[x + 2])
print(ct, mx_tr)