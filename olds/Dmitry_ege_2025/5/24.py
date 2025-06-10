def v4(x):
    s = ''
    while x > 0:
        s += str(x % 4)
        x //= 4
    return s[::-1]

for N in range(1, 10000):
    R = v4(N)
    if N % 4 == 0:
        R = '2' + R + '03'
    else:
        R = R + v4(N % 4 * 5)
    R = int(R, 4)
    if R <= 567:
        print(N)