def v5(a):
    s = ''
    while a > 0:
        s += str(a % 5)
        a //= 5
    return s[::-1]
for n in range(5,1000):
    R = v5(n)
    if n % 5 == 0:
        R = R + R[-2:]
    else:
        R = R + v5(n % 5 * 7)
    R = int(R, 5)
    if R > 200:
        print(R)
