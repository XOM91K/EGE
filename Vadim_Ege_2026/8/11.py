import itertools
c = 0
for x in itertools.product("01234567",repeat = 7):
    x = ''.join(x)
    if x[0] != '0':
        m = len([y for y in x if int(y)%2==0])
        if m == 2:
            x = x.replace('1', '#')
            x = x.replace('3', '#')
            x = x.replace('5', '#')
            if '#7' not in x and '7#' not in x and '77' not in x:
                c += 1
print(c)