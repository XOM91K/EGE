def v8(d):
    s = ''
    while d > 0:
        s += str(d % 8)
        d //= 8
    return s[::-1]

for N in range(1000, 10000):
    R = v8(N)
    for b in "0246":
        R = R.replace(b, "1")
    R = R + str(N % 8)
    R = int(R, 8)
    N2 = R
    R = v8(N2)
    for b in "0246":
        R = R.replace(b, "1")
    R = R + str(N2 % 8)
    R = int(R, 8)
    if R % 234 == 0:
        print(R)