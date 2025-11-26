import itertools
ct=0
for x in itertools.product('0123456789AB',repeat=7):
    x=''.join(x)
    if x[0] != '0':
        x=x.replace('3','*')
        x = x.replace('6', '*')
        x = x.replace('9', '*')
        x = x.replace('B', '*')
        x = x.replace('0', '*')
        x = x.replace('1', '#')
        x = x.replace('2', '#')
        x = x.replace('4', '#')
        x = x.replace('5', '#')
        x = x.replace('7', '#')
        x = x.replace('8', '#')
        x = x.replace('A', '#')

        if '**' not in x and '##' not in x:
            print(x)
            ct+=1
print(ct)