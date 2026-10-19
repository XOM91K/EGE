def v31(d):
    s = []
    while d > 0:
        s.append(d % 31)
        d //= 31
    return s[::-1]
c = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
c = v31(c)
# print(c)
sm = []
for x in c:
    if x <= 17:
        sm.append(x)
print(sum(sm))
sm = 0
for x in c:
    if x <= 17:
        sm += x
        print(x)
print('----------')
print(sm)
