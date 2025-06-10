def v7(d):
    s=""
    while d>0:
        s+=str(d%7)
        d//=7
    return s[::-1]
for N in range(10000):
    R=v7(N)
    if N %2==0:
        R="52"+R+"1"
    else:
        R = R[-1] + R[1:-1] + R[0]
        R += '15'
    R = str(int(R))
    R = int(R, 7)
    if N <= 1000 and len(str(R)) == 4:
        print(N, R)