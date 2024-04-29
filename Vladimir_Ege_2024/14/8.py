def v64(n):
    s = []
    while n > 0:
        s.append(n % 64)
        n //= 64
    return s[::-1]
d = 7 * 512 ** 3200 + 6 * 256 ** 3100 - 5 * 64 ** 3000 - 4 * 8 ** 2900 - 1542
print(v64(d).count(0))