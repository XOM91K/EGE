import itertools
ct = 0
for x in itertools.product('567', repeat=12):
    x = ''.join(x)
    if x.count('55') == 0:
        if '55' not in x:
            ct = ct + 1
            print(x)
print(ct)