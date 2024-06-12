for x in range(1000, 10000):
    c1 = int(str(x)[0]) + int(str(x)[1])
    c2 = int(str(x)[1]) + int(str(x)[2])
    c3 = int(str(x)[2]) + int(str(x)[3])
    l = [c1, c2, c3]
    l.sort()
    if l[2] == 15 and l[1] == 13:
        print(x)