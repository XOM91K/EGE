def v5(d):
    s = ''
    while d > 0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
h = []
for x in range(1, 2005):
    d = 5 ** 150 + 5 ** 98 - x
    d = v5(d)
    h.append([d.count('0'), x])
print(max(h))