l = [int(x) for x in open('17.txt')]
mx3 = sorted(l)[-3]
ct = 0
mx = 0
for x in range(len(l) - 2):
    if not(l[x] % 2 == 0 and l[x + 1] % 2 == 0 and l[x + 2] % 2 == 0):
        if (l[x] + l[x + 1] + l[x + 2]) <= mx3:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)