def f(n):
    l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
            break
    return sorted(set(l))
import itertools
# for x in range(1861, 10 ** 10, 1861):
#     print(x)
d = []
for y in range(0, 4):
    for x in itertools.product('0123456789', repeat=y):
        x = ''.join(x)
        for v1 in range(10):
            for v2 in range(10):
                chislo = '3' + str(v1) + '67' + x + '2' + str(v2) + '1'
                a = f(int(chislo))
                if len(a) > 0:
                    M = a[0] + a[-1]
                    if int(chislo) % 1861 == 0 and int(chislo) <= 10**10 and str(M)[-2:] == '52':
                        d.append([int(chislo), max(a)])
for x in sorted(d):
    print(*x)