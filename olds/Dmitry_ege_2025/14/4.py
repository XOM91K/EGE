def v5(x):
    s = ''
    while x > 0:
        s += str(x % 5)
        x //= 5
    return s[::-1]
d = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
d = v5(d)
print(sum(map(int, d)))