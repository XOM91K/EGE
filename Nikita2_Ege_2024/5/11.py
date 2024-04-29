for N in range(1, 1000):
    R = bin(N)[2:]
    if R.count('1') % 4 == 0:
        R = '10' + R
    else:
        R = '11' + R
    if R[-1] == '0':
        R += '0'
    else:
        R += '1'
    R = int(R, 2)
    if R <= 250:
        print(N)