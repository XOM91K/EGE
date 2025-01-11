def v7(d):
    s = ''
    while d > 0:
        s = str(d % 7) + s
        d //= 7
    return s

d = 8**1006 + 5**1947 + 505
d = v7(d)
print(d.count('6') * 6  - d.count('2') * 2)