import itertools
ct = 0
for x in itertools.product('0123456789abcdef', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        if len([str(d) for d in x if d in '0123456789']) == 1:
            ct += 1
print(ct)