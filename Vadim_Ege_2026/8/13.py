import itertools
ct = 0
for x in itertools.product('0123456789abcde', repeat=5):
    x = ''.join(x)
    if x[0] != '0':
        if x.count('8') == 1:
            ctB = 0
            for y in 'abcde':
                ctB += x.count(y)
            if ctB >= 2:
                ct += 1
print(ct)