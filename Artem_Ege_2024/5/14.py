for N in range(100, 1000): #243
    c1 = int(str(N)[0]) * int(str(N)[1])
    c2 = int(str(N)[1]) * int(str(N)[2])
    if min(c1, c2) == 6 and max(c1, c2) == 21:
        print(N)