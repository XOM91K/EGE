c = []
import math
for i in range(4, 10000):
    v = '8' + '7' * i
    while '57' in v or '877' in v or '777' in v:
        if '57' in v:
            v = v.replace('57', '7', 1)
        if '877' in v:
            v = v.replace('877', '75', 1)
        if '777' in v:
            v = v.replace('777', '8', 1)
    c.append(math.prod(map(int, v)))
print(max(c))