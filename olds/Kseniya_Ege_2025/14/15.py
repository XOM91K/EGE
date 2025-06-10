def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s
c = 19 ** 81 + 23 ** 709 - 4
c = v9(c)
ct = 0
for x in '1234567':
    ct += c.count('8' + x)
print(ct)
#print(c.count('81') + c.count('82') + c.count('83') + c.count('84') + c.count('85') + c.count('86') + c.count('87'))