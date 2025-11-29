for a in range(2):
    for b in range(2):
        if ((a or b) and (not(a and b))) == 1:
            print(1)