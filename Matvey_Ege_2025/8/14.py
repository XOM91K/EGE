import itertools
ct = 0
for x in itertools.product('0123456789abc', repeat=6):
    x = ''.join(x)
    if x.count('1') == 2 and x[0] != '0':
        if 'ab' not in x and 'ba' not in x and 'cb' not in x and 'bc' not in x and 'aa' not in x and 'cc' not in x and 'ac' not in x and 'ca' not in x:
            x = x.replace('0', '#')
            x = x.replace('2', '#')
            x = x.replace('4', '#')
            x = x.replace('6', '#')
            x = x.replace('8', '#')
            x = x.replace('a', '@')
            x = x.replace('b', '@')
            x = x.replace('c', '@')
            if '#@' not in x and '@#' not in x:
                ct += 1
print(ct)