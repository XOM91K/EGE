for N in range(1000, 10000):
    sm1 = int(str(N)[0]) + int(str(N)[1])
    sm2 = int(str(N)[2]) + int(str(N)[3])
    ch = int(str(min(sm1, sm2)) + str(max(sm1, sm2)))
    if ch == 117:
        print(N)