import itertools
ct = 0
for x in itertools.product('0123456789abc', repeat=6):
    x = ''.join(x)
    if x.count('1') == 2 and x[0] != '0':
        if 'aa' not in x and 'ac' not in x and 'ca' not in x and 'cc' not in x:
            if 'ab' not in x and 'ba' not in x and 'cb' not in x and 'bc' not in x:
                x = x.replace('2', '0')
                x = x.replace('4', '0')
                x = x.replace('6', '0')
                x = x.replace('8', '0')
                x = x.replace('b', 'a')
                x = x.replace('c', 'a')
                if '0a' not in x and 'a0' not in x:
                    ct += 1
print(ct)