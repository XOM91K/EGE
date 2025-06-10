for N in range(1,10000):
    R = bin(N)[2:]
    R = R.replace('0','#') #  101 1#1
    R = R.replace('1','0') #  0#0
    R = R.replace('#', '1')#  010
    R = int(R,2)
    R = abs(N - R)
    if R == 1005:
        print(N)