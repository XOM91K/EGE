def v31(d):
    s = []
    while d > 0:
        s.append(str(d % 31))
        d //= 31
    return s
c = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
c = v31(c)
#print(c.count('1') * 1 + c.count('2') * 2 +c.count('3') * 3 +c.count('4') * 4 +c.count('5') * 5 +c.count('1') * 1 +)
sm = 0
for x in range(1, 18):
    sm += c.count(str(x)) * x
print(sm)