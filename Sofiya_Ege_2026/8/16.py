import itertools
for x in itertools.product('0123456', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
