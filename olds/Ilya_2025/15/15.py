for A in range(1,1000):
    can = True
    for x in range(1,1000):
        for y in range(1,1000):
            if ((x%A==0) <=((not (x%55==0)) <= (not (y%101==0))))==0:
                can = False
                break
        if can == False:
            break
    if can:
        print(A)