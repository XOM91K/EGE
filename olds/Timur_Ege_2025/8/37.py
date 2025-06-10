import itertools
ct = 0
for x in itertools.product('01234567', repeat = 7):
    x = ''.join(x)
    if x[0] != '0':
        x = x.replace('2','@')
        x = x.replace('4', '@')
        x = x.replace('6', '@')
        x = x.replace('0', '@')
        x = x.replace('1', '#')
        x = x.replace('3', '#')
        x = x.replace('5', '#')
    if x.count('@') == 2 and x.count('#7') + x.count('7#') + x.count('77') == 0:
        ct += 1
print(ct)