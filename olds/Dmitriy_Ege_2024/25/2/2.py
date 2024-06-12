
for y in range(95632, 95701):
    l = []
    for x in range(1, int(y ** 0.5) + 1):
        if y % x == 0 and x % 2 == 0:
            l.append(x)
        if x != y // x and (y // x) % 2 == 0 and y % (y // x) == 0:
            l.append(y // x)
    if len(l) == 6:
        print(sorted(l))