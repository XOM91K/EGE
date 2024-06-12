for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 3 == 0:
        R += R[0] + R[1]
    else:
        R = bin(R.count('1') % 3 * 3)[2:] + R
    R = int(R, 2)
    if R <= 60:
        print(N)