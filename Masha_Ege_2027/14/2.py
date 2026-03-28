import string
print(string.ascii_lowercase)
# print(string.ascii_uppercase)
for x in '0123456789abcdefghijklmnopqrst':
    for y in '4':
        c1 = int(f'b{y}{x}6r94e{x}', 30)
        c2 = int(f'M{y}KGN{x}', 30)
        if (c1 + c2) % 10 == 0:
            print((c1 + c2) // 10)
