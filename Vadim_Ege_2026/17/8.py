l = [int(x) for x in open('8.txt')]
c = []
m = max(l) - min(l)
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        t = sorted([l[x], l[y]])
        g = [i for i in t if i < 0 and len(str(abs(i))) == 5 and abs(i) % 46 == 0]
        if len(g) == 1 and ((t[0] - t[1]) ** 2) % m == 0:
            c.append((t[0] - t[1]) ** 2)
print(len(c), max(c))
