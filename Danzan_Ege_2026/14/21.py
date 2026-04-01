def v7(d):
    s = ''
    while d > 0:
        s += str(d%7)
        d //= 7
    return s[::-1]
l = []
for x in range(1, 100000):
    d = 7**500 + 7**200 - 7**50 - x
    d = v7(d)
    if int(d) > 0:
        l.append(sum(map(int, d)))
print(max(l))