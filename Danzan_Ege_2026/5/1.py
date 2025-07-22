mn = 10 ** 10
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R > 151:
        mn = min(mn, R)
print(mn)
# d = '5'
# d += '1'
# d += 1
# d -= 1
# d *= 3
# d //= 3
# d %= 2
# print(d)