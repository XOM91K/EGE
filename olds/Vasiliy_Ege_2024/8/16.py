import itertools
ct = 0
for x in itertools.product('0123456789abcdefg', repeat=5):
    x = ''.join(x)
    if x[0] != "0":
        if x.count('1') <= 2:
            x = x.replace('3', '@')
            x = x.replace('5', '@')
            x = x.replace('7', '@')
            x = x.replace('9', '@')
            x = x.replace('b', '@')
            x = x.replace('d', '@')
            x = x.replace('f', '@')
            if '@1' not in x and '1@' not in x and '11' not in x:
                ct += 1
print(ct)