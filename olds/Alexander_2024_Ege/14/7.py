import string
alf = string.ascii_uppercase
mx = 0
for x in '0123456789ABCDEFGHIJKL':
    for y in '0123456789ABCDEFGHIJKL':
        c1 = int('34256' + x + '4', 22)
        c2 = int('72847' + y + '3', 22)
        if (c1 + c2) % 125 == 0:
            mx = max(mx, int(x, 22) + int(y, 22))
for x in '0123456789ABCDEFGHIJKL':
    for y in '0123456789ABCDEFGHIJKL':
        c1 = int('34256' + x + '4', 22)
        c2 = int('72847' + y + '3', 22)
        if (c1 + c2) % 125 == 0 and int(x, 22) + int(y, 22) == mx:
            print((c1 + c2) // 125)