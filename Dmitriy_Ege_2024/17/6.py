l = [int(x) for x in open('6.txt')]
ct = mx = 0
mn_1 = min([x for x in l if str(x)[-1] == '1'])
for x in range(len(l) - 1):
    if str(l[x])[-1] == str(l[x + 1])[-1]:
        if (l[x] % 3 == 0 and l[x + 1] % 3 != 0) or (l[x] % 3 != 0 and l[x + 1] % 3 == 0):
            if l[x] ** 2 + l[x + 1] ** 2 <= mn_1 ** 2:
                ct += 1
                mx = max(mx, l[x] + l[x + 1])
print(ct, mx)