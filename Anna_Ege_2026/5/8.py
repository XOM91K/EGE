def v4(n):
    s = ''
    while n >0:
        s += str(n%4)
        n//=4
    return s[::-1]
for N in range(31, 100000):
    r = v4(N)
    if len(r) % 2 == 0:
        r = r[:len(r) // 2] + '0' + r[len(r) // 2:]
    else:
        pass
    if int(r) <= 180:
        print(r, N)