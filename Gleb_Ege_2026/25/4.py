import itertools
for x in range(0, 6):
    for y in itertools.product('0123456789', repeat=x):
        y = ''.join(y)
        for z in range(10):
            ch = '32' + y + '54' + str(z) + '123'
            if int(ch) % 519 == 0:
                if '0' not in ch and len(ch) % 2 == 0:
                    plv1 = ch[:len(ch) // 2]
                    plv2 = ch[len(ch) // 2:]
                    if sum(map(int, plv1)) == sum(map(int, plv2)):
                        print(ch, int(ch) // 519)