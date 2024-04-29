k = 3
l = [[int(d) for d in x.split()] for x in open('5.txt')]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
ct = 0
mx_key = 0
for x in sl:
    sl[x] = sorted(sl[x])
    i = 1
    c_r = 0
    c_l = 0
    for j in range(1, sl[x][-1] + 2):
        if j in sl[x]:
            c_r += 1
        else:
            if c_r + c_l >= k:
                ct += 1
                mx_key = max(mx_key, int(x))
            c_l = c_r
            c_r = 0
print(ct, mx_key)

