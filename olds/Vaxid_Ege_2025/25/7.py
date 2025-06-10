import itertools
for x in range(0, 6):
    for y in itertools.product('0123456789', repeat=x):
        y = ''.join(y)
        for z in range(0, 10):
            number = '32' + y + '54' + str(z) + '123'
            if len(number) % 2 == 0 and '0' not in number:
                print(number)
