def v9(d):
    s = ''
    while d > 0:
        s = str(d % 9) + s
        d //= 9
    return s
for x in range(1, 5000):
    d = 81 ** 20 - 9 ** x + 50
    d = v9(d)
    if d.count('1') + d.count('2') * 2 + d.count('3') * 3 + d.count('4') * 4 + d.count('5') * 5 + d.count('6') * 6 + d.count('7') * 7 + d.count('8') * 8 == 138:
        print(x)