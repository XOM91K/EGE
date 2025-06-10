for x in range(1000, 10000):
    x = str(x)
    c1 = int(x[0]) + int(x[1])
    c2 = int(x[2]) + int(x[3])
    if max(c1, c2) == 17 and min(c1, c2) == 1:
        print(x)