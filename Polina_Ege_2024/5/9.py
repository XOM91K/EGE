for N in range(1000, 10000):
    if len(set(str(N))) == 4:
        R = sorted(map(int, str(N)))
        d1 = R[-1] + R[0]
        d2 = R[1] * R[2]
        if int(str(min(d1, d2)) + str(max(d1, d2))) > 85:
            print(N)
            break