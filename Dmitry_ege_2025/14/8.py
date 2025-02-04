def v25(x):
    s = []
    while x > 0:
        s.append(str(x % 25))
        x //= 25
    return s[::-1]
d = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 5 * 25 ** 4 - 2025
d = v25(d)
print(d)
print(d.count('0'))