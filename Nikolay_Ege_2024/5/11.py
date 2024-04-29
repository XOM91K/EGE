ct = 0
for N in range(128, 256, 2):
    R = oct(N)[2:]
    if sum(map(int, R)) % 2 == 0:
        R = R[:-1] + '2'
    else:
        R = '1' + R[1:]
    R = int(R, 8)
    if R >= 100:
        ct += 1
print(ct)