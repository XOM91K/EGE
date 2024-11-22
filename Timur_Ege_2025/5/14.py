for N in range(1,10000):
    R = bin(N)[2:]
    if sum(map(int, str(N))) % 2 != 0:
        R = R + '1'
    else:
        R = R + '0'
    N = int(R, 2)
    if sum(map(int, str(N))) % 2 != 0:
        R = R + '1'
    else:
        R = R + '0'
    N = int(R, 2)
    if sum(map(int, str(N))) % 2 != 0:
        R = R + '1'
    else:
        R = R + '0'
    R = int(R,2)
    if R > 2064:
        print(R)
# N = 8316
# print(sum(map(int, str(N))))