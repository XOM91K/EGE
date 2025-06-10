for N in range(1, 100000):
    R = bin(N)[2:]
    F = R.count("1")
    if N % 2 == 0:
        R += "0"
    else:
        R += "1"
    if F % 2 == 0:
        R += "0"
    else:
        R += "1"
    R = int(R, 2)
    if R > 2023:
        print(R)
