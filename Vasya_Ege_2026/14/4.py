for x in range(1, 3001):
    s = 4**210 + 4**110 - x
    c = ''
    while s > 0:
        c += str(s % 4)
        s //= 4
    c = c[::-1]
    if c.count('0') > 104:
        print(x, c.count('0'))