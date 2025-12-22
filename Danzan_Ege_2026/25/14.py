import fnmatch, itertools
for y in range(0, 6):
    for x in itertools.product('123456789', repeat=y):
        x = ''.join(x)
        for z in range(1, 10):
            chislo = '32' + x + '54' + str(z) + '123'
            if int(chislo) % 519 == 0:
                if len(chislo) % 2 == 0:
                    # 123123
                    if sum(map(int, chislo[:len(chislo) // 2])) == sum(map(int, chislo[len(chislo) // 2:])):
                        print(chislo, int(chislo) // 519)