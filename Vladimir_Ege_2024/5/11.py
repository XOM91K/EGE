for N in range(1, 10000):
    R = bin(N)[2:]
    if R.count('1') % 4 == 0:
        R = '10' + R
    else:
        R = '11' + R
    if int(R, 2) % 2 == 0:
        R += '1'
    else:
        R += '0'
    R = int(R, 2)
    if R <= 250:
        print(N)
