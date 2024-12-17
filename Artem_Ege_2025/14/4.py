def v9(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]
d = 1 * 3 ** 37 + 2 * 3 ** 23 + 3 * 3 ** 20 + 4 * 3 ** 4 + 5 * 3 ** 3 + 4 + 5
d = v9(d)
print(d.count('0'))