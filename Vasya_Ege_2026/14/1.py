import string
#print(string.printable)
for x in '0123456789ABCDEFGHIJKL':
    c = int(f'A23{x}AC0', 22) + int(f'GB{x}21670', 22)
    if c % 21 == 0:
        print(x, c // 22)