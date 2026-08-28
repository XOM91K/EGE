import itertools
for x in range(0, 6):
    for y in itertools.product('123456789', repeat=x):
        y = ''.join(y)
        for z in range(1, 10):
            ch = '32' + y + '54' + str(z) + '123'
            if int(ch) % 519 == 0:
                if len(ch) % 2 == 0:
                    pol1 = ch[:len(ch) // 2]
                    # abcnml
                    pol2 = ch[len(ch) // 2:]
                    if sum(map(int, pol1)) == sum(map(int, pol2)):
                        print(ch, int(ch) // 519)