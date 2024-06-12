d = 5 ** 2004 - 5 ** 1016 - 25 ** 508 - 5 ** 400 + 25 ** 250 - 27
s = ''
while d > 0:
    s += str(d % 5)
    d //= 5
print(s.count('4'))
print(s)