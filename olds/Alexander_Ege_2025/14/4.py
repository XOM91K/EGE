def v9(d):
    s = ''
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
n = 1 * 3 ** 37 + 2 * 3 ** 23 + 3 * 3 ** 20 + 4 * 3 ** 4 + 5 * 3 ** 3 + 4 + 5
n = v9(n)
print(n.count('0'))