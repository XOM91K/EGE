def f(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n//=3
    return s[::-1]
for n in range(1,10000):
    r = f(n)
    if n % 2 == 0:
        r = '1' + r + '00'
    else:
        r += f(r.count('1') + r.count('2') * 2)
    r = int(r,3)
    if r > 168:
        print(n)