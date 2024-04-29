sm = 0
for N in range(1000,10000):
    R = oct(N)[2:]
    for f in '02468':
        R=R.replace(f, '1')
    R += str(N % 8)
    R = int(R , 8)
    R = oct(R)[2:]
    for f in '02468':
        R = R.replace(f, '1')
    R += str(N % 8)
    R = int(R, 8)
    if R % 234 == 0:
        print(R)
