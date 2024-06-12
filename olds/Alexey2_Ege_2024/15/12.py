for A in range(1, 500):
    can = True
    for x in range(1, 500):
        for y in range(1, 500):
            if (not((x+5 < A) <=(y >A)) or (x * y >=76)) == 0:
                can = False
                break
    if can == True:
        print(A)
        break