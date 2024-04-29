for n in range(100, 1000):
    d = str(n)
    c1 = int(d[0]) * int(d[1])
    c2 = int(d[1]) * int(d[2])
    if max(c1, c2) == 21 and min(c1, c2) == 6:
        print(n)