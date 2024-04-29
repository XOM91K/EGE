for N in range(1000, 10000):
    if '0' not in str(N):
        T = sum(map(int, str(N)))
        ost = sorted([T % int(x) for x in str(N)], reverse=True)
        ost = int(''.join([str(x) for x in ost]))
        if ost > 2000:
            print(N)