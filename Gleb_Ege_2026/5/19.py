for N in range(3, 10000):
    R = hex(N)[2:]
    sm_cif = 0
    for y in R:
        if y.isdigit():
            sm_cif += int(y)
        else:
            if y == 'A':
                sm_cif += 10
            if y == 'B':
                sm_cif += 11
            if y == 'C':
                sm_cif += 12
            if y == 'D':
                sm_cif += 13
            if y == 'E':
                sm_cif += 14
            if y == 'F':
                sm_cif += 15
    if sm_cif % 2 == 0:
        R += 'f'
    else:
        R += '1'
    R = int(R, 16)
    if R <= 300:
        print(N)
