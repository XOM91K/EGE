def v7(n):
    s = []
    while n > 0:
        s.append(n % 7)
        n //= 7
    return s[::-1]
d = 7 * 49 ** 120 - 6 * 343 ** 65 - 5 * 7 ** 40
print(v7(d).count(6))
