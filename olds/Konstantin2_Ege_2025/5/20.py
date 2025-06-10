def f(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]
for n in range(1, 100000):
    r = f(n)
    if n % 3 == 0:
        r += r[::-1]
    else:
        r += f(r.count('1') +r.count('2')*2 +r.count('3')*3 +r.count('4')*4 +r.count('5')*5)
    r = int(r, 6)
    if n > 25 and r < 250:
        print(r)