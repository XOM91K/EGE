for x in range(1000, 10000): # 1 17
    x = str(x)
    s1 = int(x[0]) + int(x[1])
    s2 = int(x[2]) + int(x[3])
    if min(s1, s2) == 1 and max(s1, s2) == 17:
        print(x)