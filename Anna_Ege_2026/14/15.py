import string
print(string.ascii_uppercase)
for x in '0123456789ABCDEFGHIJKLMNOPQRS':
    c1 = int(f'463{x}7921', 29)
    c2 = int(f'8241{x}153', 29)
    if (c1 + c2) % 28 == 0:
        print((c1 + c2) // 28)