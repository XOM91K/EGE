def convert(z, x):
    d = ''
    while z > 0:
        d += str(z % x)
        z = z // x
    return d[::-1]
a = 39 * 15 ** 64 + 35 ** 450 + 74 * 43 ** 121 - 450035
maxi = -1
maxi1 = 0
for i in range(9, 32):
    h = convert(a, i)
    print(h.count('8'), i)