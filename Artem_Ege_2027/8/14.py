import itertools
k = 0
for x in itertools.product(sorted('МИНУС') , repeat = 4):
    x = ''.join(x)
    k += 1
    x = x.replace('М' , '@')
    x = x.replace('Н', '@')
    x = x.replace('С', '@')
    x = x.replace('И', '$')
    x = x.replace('У', '$')
    if x.count('@') >= x.count('$'):
        print(k)
