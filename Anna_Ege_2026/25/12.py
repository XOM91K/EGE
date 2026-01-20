dd = []
import itertools
for x in range(10):
    for y in range(10):
        for z in range(10):
            for f in range(3):
                for d in itertools.product('0123456789', repeat=f):
                    d = ''.join(d)
                    chislo = '125' + str(x) + str(y) + str(z) + '125' + d + '554'
                    if int(chislo) <= 10 ** 14 and int(chislo) % 27919 == 0:
                        dd.append([int(chislo), int(chislo) // 27919])
for x in sorted(dd):
    print(*x)