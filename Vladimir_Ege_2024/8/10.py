import itertools
ct = 0
for x in itertools.product('567', repeat=12):
    s = ''.join(x)
    if s.count('55') == 0:
        ct += 1
print(ct)