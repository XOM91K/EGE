import itertools
ct=0
for x in itertools.product('01234567', repeat=7):
    x=''.join(x)
    if x[0] != '0':
        x = x.replace('1', '*')
        x = x.replace('3', '*')
        x = x.replace('5', '*')
        if '*7' not in x and '7*' not in x and '77' not in x:
            x = x.replace('0', '!')
            x = x.replace('2', '!')
            x = x.replace('4', '!')
            x = x.replace('6', '!')
            if x.count('!')==2:
                ct+=1
print(ct)