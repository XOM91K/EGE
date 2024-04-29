for x in range(11, 10000):
    R = oct(x)[2:]
    if x % 5 == 0:
        R = R + R[0:3]
    else:
        R = R + bin(x % 5)[2:]
    if int(R, 8) >= 35000:
        print(x)
        break