for x in range(100, 1000):
    x = str(x)
    c1 = int(x[0]) + int(x[1])
    c2 = int(x[1]) + int(x[2])
    if max(c1, c2) == 17 and min(c1, c2) == 15:
        print(x)