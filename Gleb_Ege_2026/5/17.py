def v3(d):
    s = ''
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]
for N in range(1, 1000):
    R = v3(N)
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R = R + v3(sum(map(int, str(R))))
    R = int(str(R), 3)
    if R > 168:
        print(N)
