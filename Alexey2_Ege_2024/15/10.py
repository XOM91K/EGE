for A in range(1,1000):
    can = True
    for x in range(1,1000):
        if ((x % A !=0) <= ((x%28==0) <= (x % 49 !=0))) == 0:
            can = False
    if can:
        print(A)