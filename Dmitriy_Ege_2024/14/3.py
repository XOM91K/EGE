#5309
d = 4 * 8 ** 3032 + 3 * 16 ** 1956 + 870
s = ''
while d > 0:
    s += str(d % 7)
    d = d // 7
print(s.count('3') * 3 - s.count('1'))