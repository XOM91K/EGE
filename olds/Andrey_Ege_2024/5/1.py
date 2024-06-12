for x in range(100, 1000):
    l = int(str(x)[0]) + int(str(x)[1])
    r = int(str(x)[1]) + int(str(x)[2])
    if max(l, r) == 14 and min(l, r) == 12:
        print(x)