def v4(d):
    s = ''
    while d > 0:
        s += str(d % 4)
        d //= 4
    return s[::-1]
for N in range(1, 10000):
    R = v4(N)
    R = str(N % 2) + R + str(N % 3)
    R = int(R, 4)
    if 10 <= R <= 99:
        print(R)