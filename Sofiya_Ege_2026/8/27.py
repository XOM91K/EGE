import itertools

ct = 0
alf = '0123456789ABCDEFGHIJKLMNO'
for x in itertools.product(alf, repeat=4):
    x = ''.join(x)
    if x[0] != '0':
        sm = 0
        for y in x:
            sm += alf.index(y)
        if sm % 5 == 0:
            x = x.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0').replace('A', '0').replace('C',
                                                                                                                    '0').replace(
                'E', '0').replace('G', '0').replace('I', '0').replace('K', '0').replace('M', '0').replace('O',
                                                                                                          '0').replace(
                '3', '1').replace('5', '1').replace('7', '1').replace('9', '1').replace('B', '1').replace('D',
                                                                                                          '1').replace(
                'F', '1').replace('H', '1').replace('J', '1').replace('L', '1').replace('N', '1')
            if '11' not in x and '00' not in x:
                ct += 1
print(ct)
