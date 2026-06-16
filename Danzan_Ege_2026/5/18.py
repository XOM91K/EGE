for N in range(11, 100000):
    R = bin(N)[2:]
    if R.count('11') == 1:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if R <= 1500 and R > 1490:
        print(N, R)