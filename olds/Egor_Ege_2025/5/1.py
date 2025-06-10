def v3(a):
    s = ""
    while a > 0:
        s += str(a % 3)
        a //= 3
    return s[::-1]
mx = 0
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += v3(N % 3 * 5)
    R = int(R, 3)
    if R >= 290:
        print(N)

# {} SET
# [] LIST
# () TUPLE
# {} DICT