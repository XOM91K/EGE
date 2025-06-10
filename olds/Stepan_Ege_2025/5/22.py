def v4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]

# d = '1011101011'
# d = d[:len(d)//2] + '0' + d[len(d) // 2:]
# print(d)
for n in range(1, 10000):
    r = v4(n)
    if len(r) % 2 == 0:
        r = r[:len(r)//2] + '0' + r[len(r) // 2:]
    else:
        pass
    if int(r) <= 180:
        print(n)