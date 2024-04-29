for n in range(1, 10000):
    sm = 0
    r = oct(n)[2:]
    for i in str(n):
        sm += int(i)
    if sm % 2 == 0:
        r += str(n%3)
    else:
        r = max(r) + r
    r = int(r, 8)
    if r > 127:
        print(n)
        break