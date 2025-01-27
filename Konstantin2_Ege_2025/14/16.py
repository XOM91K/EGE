def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
n = 8 ** 1006 + 5 ** 1947 + 505
n = v7(n)
print(n.count('6') * 6 - n.count('2') * 2)