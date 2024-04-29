for y in range(174457, 174506):
    l = []
    for x in range(2, int(y ** 0.5) + 1):
        if y % x == 0:
            l.append(x)
            if int(y ** 0.5):
                l.append(y // x)
    if len(l) == 2:
        print(l)