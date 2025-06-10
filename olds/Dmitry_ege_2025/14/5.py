def v15(x):
    s = []
    while x > 0:
        s.append(x % 15)
        x //= 15
    return s[::-1]

d = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
d = v15(d)
print(len(set(d)))