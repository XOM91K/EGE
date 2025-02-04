l = [int(x) for x in open('8.txt')]
mn = min(l) % 3
mx = max(l) % 7
cnt = 0
mxs = []
for x in range(len(l) - 2):
    k = 0
    if l[x] % 3 == mn:
        k += 1
    if l[x + 1] % 3 == mn:
        k += 1
    if l[x + 2] % 3 == mn:
        k += 1
    if k == 1:
        q = 0
        if l[x] % 7 == mx:
            q += 1
        if l[x + 1] % 7 == mx:
            q += 1
        if l[x + 2] % 7 == mx:
            q += 1
        if q >= 2:
            cnt += 1
            mxs.append(l[x] + l[x + 1] + l[x + 2])
print(cnt, max(mxs))