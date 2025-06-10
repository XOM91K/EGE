import itertools
ct = 0
for x in itertools.product('01234567', repeat = 7):
    x = ''.join(x)
    if '17' not in x and '37' not in x and '57' not in x and '77' not in x and '71' not in x and '73' not in x and '75' not in x and x[0] != '0':
        x = x.replace('0', '$')
        x = x.replace('2', '$')
        x = x.replace('4', '$')
        x = x.replace('6', '$')
        x = x.replace('8', '$')
        if x.count('$') == 2:
            ct += 1
print(ct)