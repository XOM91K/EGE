m = 10000
l = [int(x) for x in open('1406.txt')]
l = sorted(l)
yash = []
for x in l:
    if 310 <= x <= 320:
        yash.append(x)
for x in l:
    if(sum(yash) + x) < m and (not(310 <= x <= 320)):
        yash.append(x)
print(len(yash), sum(yash))
yash = yash[::-1]
sm = sum(yash)
l = sorted(l)[::-1]
for x in yash:
    for y in l:
        if (not(310 <= x <= 320)):
            if (sm - x + y) <= m:
                sm = sm - x + y
print(sm)