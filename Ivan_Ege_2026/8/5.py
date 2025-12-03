import itertools
c = 0
for x in set(itertools.product('девиация', repeat=8)):
    x = ''.join(x)
    if 'де' in x:
        if x[0] in 'еиая' and x[-1] in 'двц':
            c += 1
print(c)