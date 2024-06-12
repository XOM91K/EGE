for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R.replace('0', '11')
    else:
        R = R.replace('1', '10')
    R = int(R, 2)
    if R <= 161:
        print(R)
