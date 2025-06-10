l = [int(x) for x in open('2.txt')]
mn = min(l)
ct = 0
mnp = []
for x in range(len(l) - 1):
    if (l[x] % 77) * (l[x + 1] % 77) == mn ** 2:
        ct += 1
        mnp.append(l[x] * l[x + 1])
print(ct, min(mnp))
# O(n ** 2)
# O(2 *n) = O(n)