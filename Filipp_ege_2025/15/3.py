for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (x % 2 != 0 or x % 13 != 0 or (x + A) >= 1000) == 0:
            flag = False
    if flag:
        print(A)