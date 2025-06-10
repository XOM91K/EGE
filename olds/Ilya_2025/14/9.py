import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQRSTUV':
    c1 = int('931' + x + '964', 32)
    c2 = int('4' + x + '51' + x + '1', 32)
    c3 = int('2861' + x + '637', 32)
    if (c1 + c2 + c3) % 31 == 0:
        print((c1 + c2 + c3) // 31)