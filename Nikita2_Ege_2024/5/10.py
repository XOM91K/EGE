for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = '1' + R + R[-2:]
    else:
        R = bin(N % 5)[2:] + R
    R = int(R, 2)
    if R <= 223:
        print(R)