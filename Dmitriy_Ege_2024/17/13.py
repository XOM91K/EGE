ct = 0
mn = 10 ** 10
l = [int(x) for x in open('13.txt')]
for x in range(len(l) - 5):
    if l[x] + l[x + 1] > 0 and l[x + 2] + l[x + 3] > 0 and l[x + 4] + l[x + 5] > 0:
        if l[x + 2] + l[x + 3] > l[x + 4] + l[x + 5] and l[x + 2] + l[x + 3] > l[x] + l[x + 1]:
            ct += 1
            mn = min(mn, l[x + 2] * l[x + 3])
print(ct, mn)