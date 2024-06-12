for n in range(11, 1000):
    r = oct(n)[2:]
    if n % 5 == 0:
        r += r[0:3]
    else:
        ost = n % 5
        r += bin(ost)[2:]
    if int(r, 8) >= 35000:
        print(n)