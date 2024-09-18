for a in range(1,400):
    can = True
    for x in range (1,400):
        if ((40 % a == 0) and (((x % a !=0) and (x % 54 ==0)) <= (x % 72 !=0))) == 0:
            can = False
            break
    if can:
        print(a)