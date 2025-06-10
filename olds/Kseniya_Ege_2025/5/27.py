def v3(d):
    s = ''
    while d > 0:
        s = str(d % 3) + s
        d //= 3
    return s
for N in range(3, 10000):
    R = v3(N)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + v3(N % 3 * 3)
    R = int(R, 3)
    if R <= 150:
        print(N)