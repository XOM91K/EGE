def v25(d):
    s = []
    while d > 0:
        s.append(d % 25)
        d //= 25
    return s[::-1]
A = 0
minx = 1000000
for x in range (1,2501):
    s = v25(25**150+25**100-x)
    if s.count(0) > 51:
        print(x)
