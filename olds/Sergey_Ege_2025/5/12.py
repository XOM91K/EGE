def v3(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]
h = []
for N in range(1, 10000):
    R = v3(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += v3(N % 3 * 4)
    R = int(R, 3)
    if R < 199:
        h.append(N)
print(max(h))