import itertools
ct = 0
for x in itertools.product('012345', repeat=3):
    x = ''.join(x)
    if x.count('5') == 1 and x[0] != '0':
        x = x.replace('0', '#')
        x = x.replace('2', '#')
        x = x.replace('4', '#')
        x = x.replace('6', '#')
        if '#5' not in x and '5#' not in x:
            print(x)
            ct += 1
print(ct)