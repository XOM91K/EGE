for N in range(10000, 100000):
    ch1 = int(str(N)[0]) + int(str(N)[2]) + int(str(N)[4])
    ch2 = int(str(N)[1]) + int(str(N)[3])
    if ch1 == 21 and ch2 == 6:
        print(N)