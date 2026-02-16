def v5(d):
    s = ''
    while d > 0:
        s = str(d % 5) + s
        d //= 5
    return s
c = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
c = v5(c)
print(sum(map(int, str(c))))
