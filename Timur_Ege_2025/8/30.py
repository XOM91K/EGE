import itertools
k = 0
for x in sorted(set(itertools.product('ПАВСИКАКИЙ', repeat = 6))):
    x = ''.join(x)
    s = x
    x = x.replace('И', '@')
    x = x.replace('А', '@')
    if x.count('@@') >= 1:
        k += 1
        if s == 'КАКААА':
            print(k,x,s)