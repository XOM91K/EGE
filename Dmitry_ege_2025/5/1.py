for x in range(1000, 10000):
    x = str(x)
    c1 = int(x[0]) * int(x[1])
    c2 = int(x[2]) * int(x[3])
    if min(c1, c2) == 12 and max(c1, c2) == 14:
        print(x)