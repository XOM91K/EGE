def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
c = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
c = v5(c)
print(c.count('1') * 1 + c.count('2') * 2 + c.count('3') * 3 + c.count('4') * 4)