def f6(n):
    c = ''
    while n > 0:
        c += str(n % 6)
        n //= 6
    return c[::-1]
for n in range(26, 1000):
    r = f6(n)
    if n % 3 == 0:
        r += r[::-1]
    else:
        r += f6(sum(map(int, r)))
    if int(r, 6) < 245:
        print(int(r, 6))