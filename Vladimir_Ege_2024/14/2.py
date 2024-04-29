d = 19 ** 81 + 23 ** 709 - 4
s = ''
while d != 0:
    s += str(d % 9)
    d //= 9
s = s[::-1]
s = s.replace('81', '#')
s = s.replace('82', '#')
s = s.replace('83', '#')
s = s.replace('84', '#')
s = s.replace('85', '#')
s = s.replace('86', '#')
s = s.replace('87', '#')
print(s.count('#'))
print(s)