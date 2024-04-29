import string
print(string.ascii_uppercase)
for p in range(22, 37):
    for q in range(32, 37):
        for x in '0123456789ABCDEFGHIJKL':
            if (int('ALE' + x, p) + int('DANOV', q)) % 2023 == 0:
                print((int('ALE' + x, p) + int('DANOV', q)) // 2023)