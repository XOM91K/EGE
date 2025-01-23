from fnmatch import *
import itertools
for y in range(5):
    for x in itertools.product('123456789', repeat=y):
        x = ''.join(x)
        for z in '123456789':
            chislo = '32' + x + '54' + z + '123'
            if int(chislo) % 519 == 0:
                if len(chislo) % 2 == 0:
                    if sum(map(int, chislo[:len(chislo) // 2])) == sum(map(int, chislo[len(chislo) // 2:])):
                        print(int(chislo), int(chislo) // 519)
# for x in range(519, 10**13, 519):
#     if fnmatch(str(x), '32*54?123'):
#         if len(str(x)) % 2 == 0 and str(x).count('0') == 0:
#             s = str(x)[:(len(str(x))//2)]
#             j = str(x)[(len(str(x))//2):]
#             if sum(map(int, s)) == sum(map(int, j)):
#                 print(x, x // 519)