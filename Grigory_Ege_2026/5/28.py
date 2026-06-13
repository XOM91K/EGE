for N in range(10,1000):
    R = bin(N)[2:]
    if R.count('11') == 1 :
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R,2)
    # if 1000< R < 1500:
    #     print(R)
    if  R == 1492 and R <= 1500:
        print(N)