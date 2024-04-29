l = [int(x) for x in open('27.txt')]
k = 73257 * 3
mx_c = 0
mx_sm = 0
for x in range(k, len(l)):
    if l[x - k] > mx_c:
        mx_c = max(mx_c, l[x - k])
        c = x - k
    if mx_c + l[x] > mx_sm:
        mx_sm = max(mx_sm, mx_c + l[x])
        mxs = [x - k, x]
mx = 0
for x in range(len(l)):
    if x not in mxs:
        mx = max(mx, l[x])
print(mx + mx_sm)