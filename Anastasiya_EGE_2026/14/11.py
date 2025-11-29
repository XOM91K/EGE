import string
print(string.ascii_letters)
for x in '0123456789abcdefghijklmnopqrstuvwxyz':
    for y in '0123456789abcdefghijklmnopqrstuvwxyz':
        c = int(f'12{x}643{y}7', 37)
        if c%36==0:
            print(y, x)