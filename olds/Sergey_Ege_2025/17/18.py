l = [int(x) for x in open("4.txt")]
mn = min([x for x in l if x % 2 == 0])
ct = 0
mn1 = 10 ** 10
for x in range(len(l) - 1):
    if (l[x] % 2 == 0 and l[x + 1] % 2 != 0) or (l[x] % 2 != 0 and l[x + 1] % 2 == 0):
        k = 0
        if abs(l[x] - l[x + 1]) == 1 and (min(l[x], l[x + 1]) + 1) % mn == 0:
            ct += 1
            mn1 = min(mn1, l[x] + l[x + 1])
print(ct, mn1)
