for n in range(1, 10000):
    b = bin(n)[2:]
    if n%5==0:
        b = '1' + b + b[-2:]
    else:
        b = bin(n%5)[2:] + b
    c = int(b,2)
    if c <= 223:
        print(c)