sm = 0
for N in range(10000, 99999):
    R = oct(N)[2:]
    R = R.replace('1', '2')
    R = R.replace('3', '2')
    R = R.replace('5', '2')
    R = R.replace('7', '2')
    R = R + str(N % 8)
    R = int(R, 8)
    R = oct(R)[2:]
    R = R.replace('1', '2')
    R = R.replace('3', '2')
    R = R.replace('5', '2')
    R = R.replace('7', '2')
    R = R + str(N % 8)
    R = int(R, 8)
    if R % 2023 == 0:
        sm += N
print(sm)