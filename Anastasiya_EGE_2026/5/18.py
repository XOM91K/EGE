for n in range(1000, 10000):
    r = oct(n)[2:]
    r = r.replace('0', '1')
    r = r.replace('2', '1')
    r = r.replace('4', '1')
    r = r.replace('6', '1')
    r += str(n % 8)
    r = int(r, 8)
    d = r
    r = oct(d)[2:]
    r = r.replace('0', '1')
    r = r.replace('2', '1')
    r = r.replace('4', '1')
    r = r.replace('6', '1')
    r += str(d % 8)
    r = int(r, 8)
    if r % 234 == 0:
        print(r)
