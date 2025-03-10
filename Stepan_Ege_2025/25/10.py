import itertools
for y in range(0, 6):
    for x in itertools.product('0123456789', repeat=y):
        x = ''.join(x)
        for z in range(0, 10):
            ch = '32' + x + '54' + str(z) + '123'
            if '0' not in ch:
                if len(ch) % 2 == 0:
                    if int(ch) % 519 == 0:
                        if sum(map(int, ch[:len(ch) // 2])) == sum(map(int, ch[len(ch) // 2:])):
                            if int(ch) < 10 ** 13:
                                print(ch, int(ch) // 519)