import itertools
ct = 0
for x in itertools.product('012345678', repeat=5):
    x = ''.join(x)
    if x.count('0') == 1 and x[0] != '0':
        x = x.replace('1', '@')
        x = x.replace('3', '@')
        x = x.replace('5', '@')
        x = x.replace('7', '@')
        if '@0' not in x and '0@' not in x:
            ct += 1
print(ct)