l = [int(x) for x in open('7.txt')]
mn_103 = 10 ** 10
for x in l:
    if x % 103 == 0:
        mn_103 = min(mn_103, x)
ct = 0
mx = 0
for x in range(len(l) - 1):
    if (l[x] + l[x + 1]) % 2 == 0:
        if abs(l[x] - l[x + 1]) % mn_103 == 0:
            ct += 1
            mx = max(mx, l[x] + l[x + 1])
print(ct, mx)