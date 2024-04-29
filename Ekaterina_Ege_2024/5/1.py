for n in range(100, 1000):
    c1 = int(str(n)[0]) * int(str(n)[1])
    c2 = int(str(n)[1]) * int(str(n)[2])
    if max(c1, c2) == 21 and min(c1, c2) == 6:
        print(n)