for N in range(1,10000):
    R = bin(N)[2:]
    if sum(map(int,str(R))) % 2 == 0:
        R = R + R[-2:]
    else:
        s = R[-2:]
        s = s.replace('1', '#')
        s = s.replace('0', '1')
        s = s.replace('#', '0')
        R = R + s
    R = int(R,2)
    if R > 154:
        print(N)