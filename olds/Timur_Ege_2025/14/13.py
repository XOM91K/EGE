def v9(a):
    s = ''
    while a > 0:
        s += str(a % 10)
        a //= 10
    return s[::-1]
d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
d = v9(d)
print(d.count('8'))