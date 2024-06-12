ct = 0
for N in range(1000,10000):
    R = str(N)
    if int(R[0]) % 2 == 0:
        R = (int(R[0])+int(R[2]))+abs(int(R[1])-int(R[3]))
    else:
        R = ''.join(sorted(R))
        R = bin(int(R))[2:].count('1')
    if R > 20:
        ct += 1
        print(N)
print(ct)
