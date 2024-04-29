import string
print(string.ascii_uppercase)
for x in '0123456789abcdefghi':
    a = int('98' + x + '79641', 19)
    b = int('36' + x + '14', 19)
    c = int('73' + x + '4', 19)
    if (a + b + c) % 18 == 0:
        print((a + b + c) // 18)