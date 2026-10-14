 def v31(d):
    s = ''
    while d > 0:
        s += str (d % 31)
        d //= 31
    return s[::-1]
c = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
c = v31(c)
if c <= 17:
    print(c)
