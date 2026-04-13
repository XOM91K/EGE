def v8(d):
    s=''
    while d>0:
        s=str(d%8)+s
        d//=8
    return s
for N in range(11,35001):
    R=v8(N)
    if N%5==0:
        R=R+R[:3]
    else:
        R=R+bin(N%5)[2:]
    R=int(R,8)
    if R>35000:
        print(N)