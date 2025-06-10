def v3(x):
    s = ''
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

for N in range(1, 10000):
    R = v3(N)
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R = R + v3(sum(map(int, str(R))))
    R = int(R, 3)
    if R > 168:
        print(N)