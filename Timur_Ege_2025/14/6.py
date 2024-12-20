def v15(a):
    s = ''
    while a > 0:
        s += str(a % 15)
        a //= 15
    return s[::-1]
d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
d = v15(d)
print(len(set(d)))
print(d)