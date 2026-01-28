for N in range(1, 10000):
    R = oct(N)[2:]
    if N % 2 == 0:
        R = R + max(R)
    else:
        R = R + oct(int(min(R)) * 2)[2:]
    R = int(R, 8)
    if R < 313:
        print(N)
# R = '16253126'
# R = R + max(R)
# print(R)
#print(max('1231141212'))