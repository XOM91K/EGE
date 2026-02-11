for N in range(1,10000):
    R=bin(N)[2:]
    if N%2==0:
        R=bin(R.count('1'))[2:]+R
    else:
        R='1'+R+'101'
    R = int(R, 2)
    if R>350:
        print(N)