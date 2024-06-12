def vtr(chislo):
    s = ''
    while chislo != 0:
        s += str(chislo % 3)
        chislo //= 3
    return s[::-1]
mn = 10**10
for N in range(1, 10000):
    R = vtr(N)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R += vtr(N % 3 * 5)
    if int(R, 3) > 133:
        mn = min(mn, int(R, 3))
print(mn)