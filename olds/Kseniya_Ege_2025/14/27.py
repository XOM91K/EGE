def v27(d):
    s = []
    while d > 0:
        s.append(d % 27)
        d //= 27
    return s
d = 7 * 729 ** 2048 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 3 * 9 ** 107 + 2017
d = v27(d)
print(sum([x for x in d if x > 17]))