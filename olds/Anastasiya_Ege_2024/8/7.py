import string, itertools
alp = string.digits + string.ascii_lowercase[0:7]
print(alp)
c = 0
for x in itertools.product(alp, repeat=5):
    x = ''.join(x)
    if x.count('1') <= 2 and x[0] != '0':
        x = x.replace('3', '@')
        x = x.replace('5', '@')
        x = x.replace('7', '@')
        x = x.replace('9', '@')
        x = x.replace('b', '@')
        x = x.replace('d', '@')
        x = x.replace('f', '@')
        if '@1' not in x and '1@' not in x and '11' not in x:
            c += 1
print(c)