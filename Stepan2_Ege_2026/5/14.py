for N in range(1, 10000):
    #37
    R = bin(N)[2:] #101101010 = 74
    if sum(map(int, str(N))) % 2 != 0:
        R += "1"
    else:
        R += "0"
    N = int(R, 2)
    if sum(map(int, str(N))) % 2 != 0:
        R += "1"
    else:
        R += "0"
    N = int(R, 2)
    if sum(map(int, str(N))) % 2 != 0:
        R += "1"
    else:
        R += "0"
    R = int(R, 2)
    if R > 2064:
        print(R)