l = [int(x) for x in open('14.txt')]
a = min(l)
q = []
b = max(l)
c = b - a
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        k = 0
        if l[x] < 0 and len(str(abs(l[x]))) == 5 and l[x] % 46 == 0:
            k += 1
        if l[y] < 0 and len(str(abs(l[y]))) == 5 and l[y] % 46 == 0:
            k += 1
        if k == 1:
            if ((l[x] - l[y]) ** 2) % c == 0:
                q.append((l[x] - l[y]) ** 2)
print(len(q), max(q))
