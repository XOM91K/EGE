def v31(d):
    s = []
    while d > 0:
        s.append(d % 31)
        d //= 31
    return s
d = 3 * 289 ** 2024 + 81  * 49 ** 121 - 9 * 16 ** 81 - 6011
d = v31(d)
sm = 0
for x in d:
    if x <= 17:
        sm += x
print(sm)