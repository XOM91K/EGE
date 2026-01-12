import itertools
for k in range(0, 6):
    for x in itertools.product('123456789', repeat=k):
        x = ''.join(x)
        for y in range(1, 10):
            chislo = '32' + x + '54' + str(y) + '123'
            if int(chislo) % 519 == 0 and int(chislo) < 10 ** 13:
                if len(chislo) % 2 == 0:
                    if sum(map(int, chislo[:len(chislo) // 2])) == sum(map(int, chislo[len(chislo) // 2:])):
                        print(int(chislo), int(chislo) // 519)