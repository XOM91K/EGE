l = [int(x) for x in open('1.txt')]
ct = mx = 0
for x in range(len(l) - 1):
    if (l[x] + l[x + 1]) % 3 == 0 and (l[x] + l[x + 1]) % 6 != 0:
        if str(l[x] * l[x + 1])[-1] == '8':
            ct += 1
            mx = max(mx, l[x] + l[x + 1])
print(ct, mx)