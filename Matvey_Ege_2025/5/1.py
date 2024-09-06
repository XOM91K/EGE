mn = 10 ** 10
l = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R > 151:
        mn = min(mn, R)
        l.append(R)
print(mn)
print(min(l))