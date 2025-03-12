for a in range(1000):
    flag = True
    for x in range(1000):
        f = (x in a) or ((x in range(10, 41)) <= (x % 6)!= 0)
        if not f:
            flag = False
            break
    if flag == True:
        print(a)