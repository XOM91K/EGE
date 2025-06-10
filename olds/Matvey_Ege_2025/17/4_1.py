l = [int(x) for x in open('4_1.txt')]
ct = 0
p = 10 ** 10
mn = min(l)
for i in range(len(l) - 1):
    if (l[i] % 77) * (l[i + 1] % 77) == mn ** 2:

        ct += 1
        p = min(p, l[i] * l[i + 1])
print(ct, p)