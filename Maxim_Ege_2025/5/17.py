mi = []
def v4(d):
    s = ''
    if d == 0:
        return '0'
    while d > 0:
        s+=str(d%4)
        d//=4
    return s[::-1]
for N in range(0,10000):
    R = v4(N)
    if N%2 == 0:
        R = '12' + R + v4(int(R[-1])*3)
    else:
        R = '13' + R + '21'
    R = int(R,4)
    if R > 50:
        mi.append(R)
print(min(mi))