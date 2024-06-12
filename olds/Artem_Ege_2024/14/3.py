import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHI':
    c1 = int('98' + x + '79641', 19)
    c2 = int('36' + x + '14', 19)
    c3 = int('73' + x + '4', 19)
    if (c1 + c2 + c3) % 18 == 0:
        print((c1 + c2 + c3) // 18)