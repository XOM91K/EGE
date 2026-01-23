def f31(n):
    s = []
    while n > 0:
        s.append(str(n % 31))
        n //= 31
    return s[::-1]


a = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
a = f31(a)
print(a.count('1') + a.count('2') * 2 + a.count('3') * 3 + a.count('4') * 4 + a.count('5') * 5 + a.count(
    '6') * 6 + a.count('7') * 7 + a.count('8') * 8 + a.count('9') * 9 + a.count('10') * 10 + a.count(
    '11') * 11 + a.count('12') * 12 + a.count('13') * 13 + a.count('14') * 14 + a.count('15') * 15 + +a.count(
    '16') * 16 + a.count('17') * 17)