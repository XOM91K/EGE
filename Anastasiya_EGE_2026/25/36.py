import itertools
for y in range(0, 6):
    for x in itertools.product('0123456789', repeat=y):
        x = ''.join(x)
        for z in range(0, 10):
            chislo = '32' + x + '54' + str(z) + '123'
            if int(chislo) % 519 == 0 and int(chislo) < 10 ** 13:
                if len(chislo)%2==0 and '0' not in chislo and sum(map(int,chislo[:(len(str(chislo))//2)]))==sum(map(int,str(chislo)[(len(str(chislo))//2):])):
                    print(chislo, int(chislo) // 519)