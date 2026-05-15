def v9(d):
    s = []
    while d > 0:
        s.append(str(d % 10))
        d //= 10
    return s
d = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
d = v9(d)
print(d.count('8'))