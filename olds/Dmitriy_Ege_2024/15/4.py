for A in range(1, 1000):
    for x in range(1, 1000):
        if ((A <= x <= A) or ((10 <= x <= 40) <= (not(x % 6 == 0)))) == False:
            break
    else:
        print(A)