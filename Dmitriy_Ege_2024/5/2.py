def vtr(chislo):
    s = ''
    while chislo != 0:
        s += str(chislo % 3)
        chislo //= 3
    return s[::-1]
for N in range(1, 10000):
    s = ''
    R = vtr(N)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R += vtr(N % 3 * 4)
    if int(R, 3) < 199:
        print(N)