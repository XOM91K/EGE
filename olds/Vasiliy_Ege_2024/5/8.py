for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3:] #добавляем 3 посл. двоич. цифры
    else:
        R = R + bin(N % 3 * 3)[2:]
    if int(R, 2) >= 76:
        print(N)