import itertools
ct = 0
for x in itertools.product('01234567', repeat=5):
    x = ''.join(x)
    #12133
    if x.count('3') <= 1 and x[0] != '0':
        x = x.replace('3', '1')
        x = x.replace('5', '1')
        x = x.replace('7', '1')
        if '11' not in x:
        # f = True
        # for y in itertools.product('1357', repeat=2):
        #     y = ''.join(y)
        #     if y in x:
        #         f = False
        #         break
        # if f == True:
            ct += 1
print(ct)