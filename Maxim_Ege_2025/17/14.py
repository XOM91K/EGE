l = [int(x) for x in open('14.txt')]
a = []
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        k = 0
        if (l[x] + l[y]) % 18 == 0:
            k += 1
        if (l[x] * l[y]) % 18 == 0:
            k += 1
        if k == 1:
            a.append((l[x] + l[y]))
print(len(a), max(a))
