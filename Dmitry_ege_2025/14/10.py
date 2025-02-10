def v9(x):
    s = ''
    while x > 0:
        s += str(x % 9)
        x //= 9
    return s[::-1]
d = 19 ** 81 + 23 ** 709 - 4
d = v9(d)
ct = 0
for x in '1234567':
    ct += d.count('8' + x)
print(ct)
#if d.count('8#') > 0 and '#' == [1-7]:
print(d.count('81') + d.count('82') + d.count('83') + d.count('84') + d.count('85') + d.count('86') + d.count('87'))
