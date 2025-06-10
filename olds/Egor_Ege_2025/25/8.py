import itertools
d = []
for i2 in range(2):
    for i in itertools.product('0123456789', repeat=i2):
        i = ''.join(i)
        for j2 in range(2):
            for j in itertools.product('0123456789', repeat=j2):
                j = ''.join(j)
                for x in range(10):
                    for y in range(10):
                        for z in range(10):
                            c = '125' + str(x) + str(y) + str(z) + '125' + i + j + '554'
                            if int(c) < 10 ** 14 and int(c) % 27919 == 0:
                                if [int(c), int(c) // 27919] not in d:
                                    d.append(([int(c), int(c) // 27919]))
for x in sorted(d):
    print(*x)

