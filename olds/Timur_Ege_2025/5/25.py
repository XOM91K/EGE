def v4(a):
    s = ''
    while a> 0:
        s += str(a % 4)
        a //= 4
    return s[::-1]
for N in range(1,10000):
    R = v4(N)
    if N % 4 == 0:
        R = '2' + R + '03'
    else:
        R = R + v4(N % 4 * 5)
    R = int(R, 4)
    if R <= 567:
        print(N)

        #R = R + v5(n % 5 * 7)
        #R = R + bin(N % 5 * 5)[2:]
        #R = R + bin(N % 3 * 3)[2:]