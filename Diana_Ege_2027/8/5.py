import itertools
ct=0
for x in itertools.product("012345678",repeat=7):
    x="".join(x)
    if x[0] != '0' and '2' not in x:
        if len(set(x)) == 7:
            x = x.replace('0', '#')
            x = x.replace('2', '#')
            x = x.replace('4', '#')
            x = x.replace('6', '#')
            x = x.replace('8', '#')
            x = x.replace('1', '@')
            x = x.replace('3', '@')
            x = x.replace('5', '@')
            x = x.replace('7', '@')
            if '##' not in x and '@@' not in x:
                print(x)
                ct += 1
print(ct)