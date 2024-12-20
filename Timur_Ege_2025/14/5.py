def v9(a):
    s = ''
    while a > 0:
        s += str(a % 9)
        a //= 9
    return s[::-1]
d = 1 * 3 ** 37 + 2 * 3 ** 23 + 3 * 3 ** 20 + 4 * 3 ** 4 + 5 * 3 ** 3 + 4 + 5
d = v9(d)
print(d.count('0'))