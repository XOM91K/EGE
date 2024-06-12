d = 36
l = []
for x in range(1, int(d ** 0.5) + 1):
    if d % x == 0:
        l.append(x)
        l.append(d // x)
print(sorted(set(l)))