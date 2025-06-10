def in4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]
for N in range(1, 100000):
    R = in4(N)
    if len(R) % 2 == 0:
        R = R[:len(R) // 2] + '0' + R[len(R) // 2 + 1:]
    R = int(R)
    if R <= 180:
        print(N)