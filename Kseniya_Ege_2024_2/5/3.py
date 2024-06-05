def per(n):
    os = ''
    while n > 0:
        os = os + str(n%3)
        n = n // 3
    return os[::-1]
for n in range(1, 100):
    nm = per(n)
    if (nm.count('1') + nm.count('2') * 2) % 2 == 0:
        nm = nm + '0'
        nm = '2' + nm[2:]
    else:
        nm = nm + '1'
        nm = '20' + nm[2:]
    r = int(nm, 3)
    if r > 75 and r <= 78:
        print(r, n)