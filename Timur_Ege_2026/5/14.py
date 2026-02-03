for N in range(154,10000):
    R=bin(N)[2:]
    if R.count('0')== R.count('1'):
        R+=R[-1]
    if R.count('0')== R.count('1'):
        R+=R[-1]
    if R.count('0')== R.count('1'):
        R+=R[-1]
    R=int(R,2)
    if N%7==0 and N > 154:
        print(N)