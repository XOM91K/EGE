import itertools
number = 0
for x in itertools.product('ЩОГБА', repeat=6):
    x = ''.join(x)
    number = number + 1
    if x == 'ОБЩАГА':
        print(number)