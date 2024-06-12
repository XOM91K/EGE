def des(l, o):
    d = 0
    for x in range(len(l)):
        d += l[x] * o ** (len(l) - x - 1)
    return d
sm = 0
for x in range(0, 58):
    for y in range(72):
        dd = (des([3,4,x,5], 58) + des([1,2,x,7], 61) + des([x,4,5,6], 67) - des([x,5,y,7], 72))
        if (dd > 0) and (dd % 363 == 0):
            print(x, y)
            sm += x + y
print(sm)