for N in range(10000):
    R = bin(N)[2:]
    if N %2==0:
        R="1"+R+"00"
    else:
        R+=bin(R.count('1'))[2:]
    R=int(R,2)
    if R>205:
        print(N)