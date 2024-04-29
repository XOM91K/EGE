import itertools
for n in range(10):
    for d in itertools.product('0123456789', repeat=3):
        if int('1' + str(n) + '2139' + ''.join(d) + '4') % 2023 == 0 and int('1' + str(n) + '2139' + ''.join(d) + '4') < 10**10:
            print(int('1' + str(n) + '2139' + ''.join(d) + '4'), int('1' + str(n) + '2139' + ''.join(d) + '4') // 2023)