def v7(d):
    s = ''
    while d > 0:
        s += str(d%7)
        d//=7
    return s[::-1]
for x in range(1, 2030):
    d = 7**170 + 7**100 - x
    d = v7(d)
    if d.count('0') == 71:
        print(x)