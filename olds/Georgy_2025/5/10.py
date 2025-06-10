def vtroichnuyu(chislo):
    s = ''
    while chislo > 0:
        s += str(chislo % 3)
        chislo //= 3
    return s[::-1]
for N in range(1, 10000):
    R = vtroichnuyu(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += vtroichnuyu(N % 3 * 4)
    R = int(R, 3)
    if R < 199:
        print(N)
