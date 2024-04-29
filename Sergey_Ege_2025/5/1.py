for n in range(1000, 10000):
    c1 = int(str(n)[0]) + int(str(n)[1])
    c2 = int(str(n)[1]) + int(str(n)[2])
    c3 = int(str(n)[2]) + int(str(n)[3])
    if max(c1, c2, c3) == 13 and c1 + c2 + c3 - max(c1, c2, c3) - min(c1, c2, c3) == 6:
        print(n)
