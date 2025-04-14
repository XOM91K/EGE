s = []
for n in range(3, 10000):
    a = '8' + '7' * n
    while '57' in a or '877' in a or '777' in a:
        if '57' in a:
            a = a.replace('57', '7', 1)
        if '877' in a:
            a = a.replace('877', '75', 1)
        if '777' in a:
            a = a.replace('777', '8', 1)
    r = (8 ** a.count('8')) * (7 ** a.count('7')) * (5 ** a.count('5'))
    s.append(r)
print(max(s))
# 3433