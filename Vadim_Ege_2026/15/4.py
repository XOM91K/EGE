for An in range(47, 117):
    for Af in range(90, 91):
        can = True
        for x in range(1, 1000):
            if ((47 <= x <= 115) <= (((not(An + 1 <= x <= Af - 1)) and (24 <= x <= 90))) <= (not(47 <= x <= 115))) == 0:
                can = False
                break
        if can:
            print(Af - An)