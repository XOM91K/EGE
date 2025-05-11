a = []
import math
for n in range(4,10001):
    s = '8' + '7' * n
    while '57' in s or '877' in s or '777' in s:
        if '57' in s:
            s = s.replace('57','7',1)
        if '877' in s:
            s = s.replace('877','75',1)
        if '777' in s:
            s = s.replace('777','8',1)
    # p = s.count('7') * 7 * s.count('5') * 5 * s.count('8') * 8
    # a.append(p)
    a.append(math.prod(map(int, s)))
print(max(a))
# 3372 = 126
# 3 ** s.count('3') +