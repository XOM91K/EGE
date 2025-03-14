# for x in range(7777, 10 ** 9, 7777):
import itertools
for x in itertools.product('2468', '13579', '02468', '02468', '13579', '02468', '13579'):
    x = ''.join(x)
    x += '77'
    if int(x) % 7777 == 0:
        print(x, int(x) // 7777)