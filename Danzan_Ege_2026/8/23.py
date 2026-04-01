import itertools
ct = 0
for x in itertools.product('0123456789abcdef', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        # 22445  22345 => 11134 78999
        if sorted(x).count(sorted(x)[2]) < 3:
            if '1' in x or '4' in x or '9' in x:
                ct += 1
print(ct)