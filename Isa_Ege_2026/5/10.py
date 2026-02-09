d = []
def v12(d):
    alf = '0123456789ab'
    s = ''
    while d > 0:
        s += alf[d % 12]
        d //= 12
    return s[::-1]
for N in range(1, 10000):
    R = v12(N)
    if N % 4 == 0:
        R = '2' + R + '64'
    else:
        R += max(R)
    R = int(R, 12)
    if R > 1799:
        d.append(R)
print(min(d))
# s = '0123456789ab'
# print(max(s))
# print(ord('0')) # ASCII
# print(ord('b'))
#print(ord('б'))
# print(chr(15578))