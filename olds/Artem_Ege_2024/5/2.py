for x in range(1000, 10000):
    # => 613
    c1 = int(str(x)[0]) + int(str(x)[1])
    c2 = int(str(x)[1]) + int(str(x)[2])
    c3 = int(str(x)[2]) + int(str(x)[3])
    if max(c1, c2, c3) == 13 and c1 + c2 + c3 - max(c1, c2, c3) - min(c1, c2, c3) == 6:
        print(x)