mx = 0
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R < 170:
        mx = max(mx, R)
print(mx)
# {} SET
# [] LIST
# () TUPLE
# {} DICT