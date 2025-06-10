for N in range(1000, 10000):
    sm1 = int(str(N)[0]) + int(str(N)[1])
    sm2 = int(str(N)[1]) + int(str(N)[2])
    sm3 = int(str(N)[2]) + int(str(N)[3])
    l = sorted([sm1, sm2, sm3])
    if l[1] == 12 and l[2] == 15:
        print(N, l)
