def pt(n):
    r = ''
    while n > 0:
        r = str(n % 5) + r
        n //= 5
    return r
for n in range(5, 100):
    r = pt(n)
    if n % 5 == 0:
        r += r[-2:]
    else:
        r += pt(7 * (n % 5))
    if int(r, 5) > 200:
        print(int(r, 5))