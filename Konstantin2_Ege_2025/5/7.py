for N in range(1000, 10000):
    #5431 - 320
    #???? - 1214
    pr1 = int(str(N)[0]) * int(str(N)[1])
    pr2 = int(str(N)[2]) * int(str(N)[3])
    if max(pr1, pr2) == 14 and min(pr1, pr2) == 12:
        print(N)