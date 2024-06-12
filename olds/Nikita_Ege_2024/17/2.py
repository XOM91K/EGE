l = [int(x) for x in open('2.txt')]
mx_0f = max([x for x in l if hex(x)[-2:] == '0f'])
mx = ct = 0
for x in range(len(l) - 1):
    if ((l[x] % 7 == 0 and l[x + 1] % 7 != 0) or (l[x + 1] % 7 == 0 and l[x] % 7 != 0)) and (l[x] + l[x + 1]) % mx_0f == 0:
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)