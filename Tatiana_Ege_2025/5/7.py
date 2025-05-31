r = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 != 0:
        R = R.replace('1', '111')
    else:
        R = R.replace('0', '000')
    if int(R, 2) > 701 and int(R, 2) < 1000:
        print(N, int(R, 2))
        r.append([N, int(R, 2)])
#print(sorted(r, key=lambda x: x[1]))