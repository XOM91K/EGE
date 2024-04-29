d = 81 ** 79 + 75 ** 2022 - 12 ** 35
s = ''
while d > 0:
    s += str(d % 5)
    d //= 5
s = s[::-1]
s = s.replace('41', 'x')
s = s.replace('42', 'x')
s = s.replace('43', 'x')
print(s.count('x'))