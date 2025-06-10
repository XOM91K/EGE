for i in range(11, 100000):
    a = i
    b = oct(a)[2:]
    if a % 5 == 0:
        b += b[:3]
    else:
        b += bin(a%5)[2:]
    b = int(b, 8)
    if b >= 35000:
        print(a)