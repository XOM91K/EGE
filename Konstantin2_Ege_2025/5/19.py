def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
i = 0
for N in range(3, 10000):
    R = v3(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        i = N % 3 * 3
        R = R + v3(i)
    R = int(R, 3)
    if R <= 150:
        print(N)