# d = d + 1
# d += 1
# d = d * 2
# d *= 2
# d = d / 2
# d /= 2
def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
d = v5(d)
print(sum([int(y) for y in d]))