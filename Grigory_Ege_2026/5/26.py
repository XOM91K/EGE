for N in range(3,10000):
    R = hex(N)[2:]
    sm_cif = 0
    for y in R:
        sm_cif += int(y, 16)
    if sm_cif % 2 == 0 :
        R += 'f'
    else:
        R += '1'
    R = int(R, 16)
    if R <= 300:
        print(N)