d = (7 ** 160 * 7 ** 90) - (14 ** 150 + 2 ** 13)
s = ''
while d > 0:
    s += str(d % 7)
    d //= 7
s = s[::-1]
print(s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5)