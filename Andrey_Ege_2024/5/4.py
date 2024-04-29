for N in range(2, 1000):
    R = bin(N)[2:]
    R = R + R[-2]
    R = R + R[1]
    R = int(R, 2)
    if R <= 190:
        print(N)