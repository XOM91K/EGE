import itertools
ct = 0
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x[0] != '0':
        if x[-1] == '1' or x[-1] == '2' or x[-1] == '4' or x[-1] == '5' or x[-1] == '7' or x[-1] == '8':
            x = x.replace('1', '!')
            x = x.replace('3', '!')
            x = x.replace('5', '!')
            x = x.replace('7', '!')
            if x[0] != '!' and x.count('6') >= 1:
                ct += 1
print(ct)
