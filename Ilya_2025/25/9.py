import itertools
for y in range(0, 5, 2):
    for x in itertools.product('123456789', repeat=y):
        x = ''.join(x)
        for z in '123456789':
            d = '32' + x + '54' + z + '123'
            if int(d) % 519 == 0:
                if len(d) % 2 == 0:
                    if sum(map(int, d[:len(d) // 2])) == sum(map(int, d[len(d) // 2:])):
                        print(int(d), int(d) // 519)
                        break

