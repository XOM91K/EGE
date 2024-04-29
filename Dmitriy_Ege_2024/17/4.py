l = [int(x) for x in open('4.txt')]
ct = 0
mx = 0
for x in range(len(l) - 2):
    a = l[x]
    b = l[x + 1]
    c = l[x + 2]
    d = sorted([a,b,c])
    if d[2] ** 2 < (d[0] ** 2 + d[1] ** 2):
        ct += 1
        mx = max(mx, sum(d))
print(ct, mx)