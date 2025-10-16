for A in range(0,1000):
    can = True
    for x in range(1,1000):
        for y in range(1,1000):
            if  ((x-3*y<A) or (y>400) or (x>56)) == 0 :
                can = False
                break
        if can == False:
            break
    if can :
        print(A)
        break