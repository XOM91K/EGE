def v5(n):
    s = ''
    if n == 0:
        return '0'
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]

for n in range(1, 10000):
    r = v5(n)
    if n % 2 == 0:
        r = r + v5(int(r[-1]) * 3)
    else:
        r = r[-1] + r[1:-1] + r[0] + '1'
    if str(int(r)).count('0') == 4:
        print(n)
# r = '000000000010101010101010100'
# print(str(int(r)))