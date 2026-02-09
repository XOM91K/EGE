for N in range(3, 10000):
    R = hex(N)[2:]
    print(R)
    sm_cif = 0
    for x in R:
        sm_cif += int(x, 16)
    if sm_cif % 2 == 0:
        R = str(R) + 'F'
    else:
        R = str(R) + '1'
    R = int(R, 16)
    if R <= 300:
        print(N, R)
