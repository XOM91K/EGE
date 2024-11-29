import itertools
ct = 0
for x in itertools.product('0123456', repeat=6):
    x = ''.join(x)
    #if int(x[-1]) >= 4:
    if x[0] != '0' and x[-1] not in '0123':
        # x = x.replace('2', '0')
        # x = x.replace('4', '0')
        # x = x.replace('6', '0')
        # x = x.replace('3', '1')
        # x = x.replace('5', '1')
        # x = x.replace('7', '1')
        # if x.count('0') == x.count('1'):
        if x.count('2') + x.count('0') + x.count('4') + x.count('6') == 3:
            ct += 1
            print(x)
print(ct)