def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]

for N in range(1, 10000):
    R = v3(N)
    # R = 22222
    if (R.count('1') + R.count('2') * 2) % 3 == 0:
        R = '20' + R
    else:
        R = '10' + R
    R = int(R, 3)
    if R < 100:
        print(N)

# s = '8112481269041264091204861240912481264912486190241903'
# print(s.count('8') * 8 + s.count('1') + s.count('3') * 3 + s.count('4') * 4 + s.count('5') * 5 + s.count('6') * 6 + s.count('7') * 7 + s.count('9') * 9 + s.count('2') * 2)
# print(sum(map(int, s)))