for N in range(1000, 10000):
    c1 = int(str(N)[0]) * int(str(N)[1])
    c2 = int(str(N)[2]) * int(str(N)[3])
    if c1 > c2:
        R = str(c2) + str(c1)
    else:
        R = str(c1) + str(c2)
    if R == '1214':
        print(N)