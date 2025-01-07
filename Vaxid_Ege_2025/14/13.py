import  string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLM':
    c1 = int('11353' + x + '12', 23)
    c2 = int('135' + x + '21', 23)
    if (c1 + c2) % 22 == 0:
        print(x, (c1 + c2) // 22)
#for x in