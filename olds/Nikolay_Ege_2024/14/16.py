import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJ':
    for y in '0123456789ABCDEFGHIJ':
        c1 = int('5' + y + '4' + x + y + '4HJ4', 20)
        c2 = int('4' + y + '6B' + y + x + '1', 20)
        if (c1 + c2) % 15 == 0:
            c1 = int('5' + '8' + '4' + x + '8' + '4HJ4', 20)
            c2 = int('4' + '8' + '6B' + '8' + x + '1', 20)
            print((c1 + c2) // 15, x)