for x in '0123456789abcdefghijkl':
    a = int('18' + x + '89957', 22)
    b = int('80' + x + '33', 22)
    c = int('521' + x + '6', 22)
    if (a + b + c) % 21 == 0:
        print((a + b + c) // 21)
# for x in range(97, 150):
#     print(chr(x))