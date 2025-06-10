l = [int(x) for x in open('14.txt')]
mn = min(l)
ct = 0
mn2 = 10 ** 10
for x in range(len(l) - 1):
    if (l[x] % 77) * (l[x + 1] % 77) == mn ** 2:
        ct += 1
        mn2 = min(mn2, l[x] * l[x + 1])
print(ct, mn2)