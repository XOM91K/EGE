#7067 на полякове
import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLM':
    k = 0
    for y in '0123456789ABCDEFGHIJKLM':
        c1 = int('9IE3'+y+x, 23)
        c2 = int('J5'+y+'B'+x+'L1',23)
        if (c1 + c2) % 13 == 0:
            k += 1
    if k == 23:
        c1 = int('9IE33' + x, 23)
        c2 = int('J53' + 'B' + x + 'L1', 23)
        print((c1 + c2) // 13)