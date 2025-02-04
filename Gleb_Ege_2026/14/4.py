def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]


n = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
n = v5(n)
print(sum(map(int, n)))