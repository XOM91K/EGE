def pt(n):
    r = ''
    while n > 0:
        r = str(n % 5) + r
        n //= 5
    return r
for n in range(1, 10000):
    r = pt(n)
    if n % 25 == 0:
        r = r + r[-3:]
    else:
        r += pt(int(r) % 25)
    if int(r, 5) > 10000:
        print(n)