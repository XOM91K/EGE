l = [int(x) for x in open('7.txt')]
mn_1 = 10 ** 10
ct = mx = 0
for x in l:
    if abs(x) % 10 == 1:
        mn_1 = min(mn_1, x)
for x in range(len(l) - 1):
    if abs(l[x]) % 10 == abs(l[x + 1]) % 10:
        if (l[x] % 3 == 0 and l[x + 1] % 3 != 0) or (l[x + 1] % 3 == 0 and l[x] % 3 != 0):
            if l[x] ** 2 + l[x + 1] ** 2 <= mn_1 ** 2:
                ct += 1
                mx = max(mx, l[x] + l[x + 1])
print(ct, mx)