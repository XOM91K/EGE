mx = []
for n in range(4, 10000):
    s = '8' + '7' * n
    while '57' in s or '877' in s or '777' in s:
        if '57' in s:
            s = s.replace('57', '7', 1)
        if '877' in s:
            s = s.replace('877', '75', 1)
        if '777' in s:
            s = s.replace('777', '8', 1)
    pr = 1
    for x in s:
        pr *= int(x)
    mx.append(pr)
# print(max(mx))
# import math
# s = '129371239'
# print()
# print(math.prod(list(map(int, s))))
# s = '129371239'
# pr = 1
# for x in s:
#     pr *= int(x)
# print(pr)