def v27(d):
    s = []
    while d > 0:
        s.append(str(d % 27))
        d //= 27
    return s

c = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
c = v27(c)
print(c)
print(c.count('2') * 2 + c.count('4') * 4 + c.count('6') * 6 + c.count('8') * 8 + c.count('10') * 10 + c.count('12') * 12 + c.count('14') * 14 + c.count('16') * 16 + c.count('18') * 18 + c.count('20') * 20 + c.count('22') * 22 + c.count('24') * 24)
