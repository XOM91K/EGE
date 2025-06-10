s = set()
for N in range(265432097, 265432097 + 1):
    d = N
    R = bin(N)[2:]
    for x in range(3):
        if sum([int(d) for d in str(N)]) % 2 != 0:
            R += '1'
        else:
            R += '0'
        N = int(R, 2)
    print(d, bin(d)[2:],N, R)
print(len(s))
#123456790
#265432097