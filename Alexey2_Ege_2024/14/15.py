def v7(n):
    d = []
    while n > 0:
        d.append(n % 7)
        n //= 7
    return d[::-1]
g = 8 * 343 ** 5 + 9 * 49 ** 8 - 48
print(v7(g).count(6))