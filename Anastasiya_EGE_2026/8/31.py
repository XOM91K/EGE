import itertools
ct = 0
for x in itertools.product('123456789abcde', repeat = 6):
    x = ''.join(x)
    x = x.replace('a', '@')
    x = x.replace('b', '@')
    x = x.replace('c', '@')
    x = x.replace('d', '@')
    x = x.replace('e', '@')
    if x.count('@')<=4:
        ct += 1
print(ct * 21)