l = [int(x) for x in open('8.txt')]
sm = []
t = 0
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        t += 1
        k = 0
        if (l[x] + l[y]) % 18 == 0:
            k += 1
        if (l[x] * l[y]) % 18 == 0:
            k += 1
        if k == 1:
                sm.append(l[x] + l[y])
print(len(sm), max(sm))
print(t)