import itertools
ct=0
for x in itertools.product('0123456', repeat=6):
    x=''.join(x)
    if x[0] != '0':
        if x[-1]!='0' and x[-1]!='1' and x[-1]!='2' and x[-1]!='3':
            x = x.replace('0', '!')
            x = x.replace('2', '!')
            x = x.replace('4', '!')
            x = x.replace('6', '!')
            x = x.replace('1', '%')
            x = x.replace('3', '%')
            x = x.replace('5', '%')
            if x.count('!')==3 and x.count('%') == 3:
                ct += 1
print(ct)
