import itertools
ct = 0
for x in itertools.product('01234567', repeat=7):
    x = ''.join(x)
    if x[0] != '0':
        if (x.count('0') + x.count('2') + x.count('4') + x.count('6')) == 2:
            x = x.replace('1', '#')
            x = x.replace('3', '#')
            x = x.replace('5', '#')
            if '#7' not in x and '7#' not in x:
                ct += 1
print(ct)