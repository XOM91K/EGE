def v9(x):
    s = ''
    while x > 0:
        s += str(x % 9)
        x //= 9
    return s[::-1]
d = 1 * 3 ** 37 + 2 * 3 ** 23 + 3 * 3 ** 20 + 4 * 3 ** 4 + 5 * 3 ** 3 + 4 + 5
#d = 2473 # => 3347
print(v9(d).count('0'))