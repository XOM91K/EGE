def v4(n):
    d = ""
    while n > 0:
        d += f"{n % 4}"
        n = n // 4
    return d[::-1]


for N in range(1, 10000):
    R = v4(N)
    if len(R) % 2 == 0:
        ln = len(R)
        R = R[:ln // 2] + '0' + R[ln // 2:]
    if int(R) <= 180:
        print(N)
