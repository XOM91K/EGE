for N_n in range(1, 10000):
    R = bin(N_n)[2:]
    if N_n % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N_n % 3 * 3)[2:]
    R = int(R, 2)
    if R < 170:
        print(R)