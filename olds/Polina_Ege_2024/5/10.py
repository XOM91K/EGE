for N in range(1000, 10000):
    if len(set(str(N))) == len(str(N)):
        d = sorted(map(int, str(N)))
        sm = d[0] + d[-1]
        pr = d[1] * d[2]
        R = int(str(min(sm, pr)) + str(max(sm, pr)))
        if R > 85:
            print(N)