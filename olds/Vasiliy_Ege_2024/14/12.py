def v49(n):
    s = []
    while n > 0:
        s.append(n % 49)
        n = n // 49
    return s[::-1]

x = sum(v49(abs((18 * (7 ** 108)) - (5 * (49 ** 76)) + (343 ** 35) - 50)))
print(x)