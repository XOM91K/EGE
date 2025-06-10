import itertools
for x in range(0, 5):
    for z in range(0, 5):
        for y1 in itertools.product('0123456789', repeat=z):
            for y in itertools.product('0123456789', repeat=x):
                y = ''.join(y)
                y1 = ''.join(y1)
                for v1 in '0123456789':
                    for v2 in '0123456789':
                        for v3 in '0123456789':
                            number = '125' + v1 + v2 + v3 + '125' + y1 + y + '554'
                            if int(number) % 27919 == 0 and int(number) <= 10 ** 14:
                                print(number, int(number) // 27919)