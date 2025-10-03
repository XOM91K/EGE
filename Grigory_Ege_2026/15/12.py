m = []
for A in range(0,1000):
    can = True
    for x in range(1,1000):
        for y in range(1,1000):
            if (x + y <=24 or y<=x-2 or y >= A) == 0 :
                can = False
                break
        if can == False:
            break
    if can :
        m.append(A)
print(max(m))