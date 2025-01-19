def v7(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]
d = 8 ** 1006 + 5 ** 1947 + 505
d = v7(d)
print(d.count('2') * 2 - d.count('6') * 6)