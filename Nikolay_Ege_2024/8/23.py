import itertools
ct = 0
for x in itertools.product('ВОЗДУХ', repeat=5):
    x = ''.join(x)
    if (x.count('О') + x.count('У')) == 1:
        x = x.replace('В', '*')
        x = x.replace('Х', '*')
        x = x.replace('О', '#')
        x = x.replace('У', '#')
        if '*#' not in x and '#*' not in x:
            ct += 1
print(ct)