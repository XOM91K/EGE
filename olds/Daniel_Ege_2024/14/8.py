import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJ':
    for y in '0123456789ABCDEFGHIJ':
        t = int('B' + y + '11CB' + x + 'G17', 20) + int('8A' + x + '17', 20)
        if t % 107 == 0:
            print(x, t // 107)