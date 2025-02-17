
l = []
def v6(d):
    s = ''
    while d > 0:
        s += str(d % 6)
        d //= 6
    return s[::-1]
for x in range(1, 10000):
    c1 = 6 ** 900 + 6 ** 10 - x
    c1 = v6(c1)
    if c1.count('3') == c1.count('5'):
        l.append(x)
print(min(l))