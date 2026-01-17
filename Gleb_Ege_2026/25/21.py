import itertools
d = []
for y in range(0, 3):
    for x in itertools.product('0123456789', repeat=y):
        x = ''.join(x)
        for v1 in range(10):
            for v2 in range(10):
                for v3 in range(10):
                    chislo = '125' + str(v1) + str(v2) + str(v3) + '125' + x + '554'
                    if int(chislo) % 27919 == 0 and int(chislo) <= 10**14:
                        d.append([int(chislo), int(chislo)//27919])
for x in sorted(d):
    print(*x)