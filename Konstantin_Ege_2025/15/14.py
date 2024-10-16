ct = 0
B = list(range(40, 61))
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if (((x % 13 == 0) <= (x not in B)) or (A < x + 20)) == 0:
            can = False
            break
    if can == True:
        print(A)