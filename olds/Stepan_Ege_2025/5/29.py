def v8(n):
    s = ''
    while n > 0:
        s += str(n % 8)
        n //= 8
    return s[::-1]

for n in range(1, 1000):
    r = oct(n)[2:]
    if n % 2 == 0:
        r = r + oct(int(max(str(r))))[2:]
    else:
        r = r + oct(int(min(str(r))) * 2)[2:]
    r = int(r, 8)
    if r < 313:
        print(n)
print(max('01234567'))