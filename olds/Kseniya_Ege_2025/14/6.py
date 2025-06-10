def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s
d = 1 * 3 ** 37 + 2 * 3 ** 23 + 3 * 3 ** 20 + 4 * 3 ** 4 + 5 * 3 ** 3 + 4 + 5
d = v9(d)
print(d.count('0'))