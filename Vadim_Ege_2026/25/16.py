import itertools
d = []
# 125???125**554
for y in range(0, 3):
    for x in itertools.product('0123456789', repeat=y):
        x = ''.join(x)
        for c1 in range(10):
            for c2 in range(10):
                for c3 in range(10):
                    chislo = '125' + str(c1) + str(c2) + str(c3) + '125' + x + '554'
                    if int(chislo) % 27919 == 0 and int(chislo) <= 10 ** 14:
                        d.append([int(chislo), int(chislo) // 27919])
d = sorted(d)
for x in d:
    print(*x)