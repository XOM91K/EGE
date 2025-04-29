alf = '0123456789abcde'
def v15(d):
    s = ''
    while d > 0:
        s = alf[d % 15] + s
        d //= 15
    return s
d = []
for N in range(15, 10000):
    R = v15(N)
    if N % 15 == 0:
        R += R[:2]
    else:
        R += v15(N % 15 * 13)
    R = int(R, 15)
    if R > 700:
        d.append(R)
print(min(d))