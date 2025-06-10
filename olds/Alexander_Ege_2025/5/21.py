for N in range(1,10000):
    R=bin(N)[2:]
    if R.count('1') % 2 == 0:
        R += R[-2:]
    else:
        d = R[-2:]
        d = d.replace('0', '#')
        d = d.replace('1', '0')
        d = d.replace('#', '1')
        #R[-2:][::-1]
        R += d
    R=int(R,2)
    if R > 154:
        print(N)