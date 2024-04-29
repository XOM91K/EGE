def pt(d):
    s =''
    while d >0:
        s += str(d % 5)
        d //= 5
    return s[::-1]
for N in range(1, 10000):
    d2 = int(pt(N)[::-1], 5)
    R = abs(d2 - N)
    if R == 100:
        print(N)