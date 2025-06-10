# def v8(d):
#     s=""
#     while d>0:
#         s+=str(d % 8)
#         d//=8
#     return s[::-1]
for N in range(1,10000):
    R=oct(N)[2:]
    if N%2==0:
        R += max(R)
    else:
        R += oct(int(min(R)) * 2)[2:]
    R = int(R, 8)
    if R < 313:
        print(N)