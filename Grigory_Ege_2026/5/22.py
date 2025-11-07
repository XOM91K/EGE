d = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R.replace('0', '1')
    else:
        sr = R[1:].replace('1', '00')
        R = '1' + sr
    R = int(R, 2)
    if R == 512:
        print(N)
        d.append(R)

def c8(x):
    s = ''
    while x > 0:
        s = str(x % 8) + s
        x = x // 8
    return s
for n in range(1, 10_000_000):
    b = c8(n)
    if b[0] == '5':
        b = b.replace('2', '*').replace('1', '2').replace('*', '1')
        b = '11' + b
    else:
        b = b + '10'
        b = '2' + b[1:]
    r = int(b, 8)
    if r < 1354:
        print(n)