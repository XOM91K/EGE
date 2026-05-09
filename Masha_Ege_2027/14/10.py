def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
d = 53 ** 123 + 65 ** 2222 - 172 ** 12
d = v7(d)
d = d.replace('1', '#').replace('2', '#').replace('3', '#').replace('4', '#').replace('5', '#')
print(d.count('6#'))