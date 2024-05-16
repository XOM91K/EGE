def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if N % 2 == 0:
        R = R.replace('1', '2')
        R += R[-2:]
    else:
        R += str(N % 3)
        R += str(N % 3)
    R = int(R, 3)
    if R <= 1165:
        print(N)