d = []
for N in range(1,10000):
    R = bin(N)[2:]
    if sum(map(int, str(N))) % 2 != 0:
        R += '1'
    else:
        R += '0'
    if sum(map(int, str(int(R, 2)))) % 2 != 0:
        R += '1'
    else:
        R += '0'
    if sum(map(int, str(int(R, 2)))) % 2 != 0:
        R += '1'
    else:
        R += '0'
    R = int(R, 2)
    if R > 2064:
        print(R)
        d.append(R)
print(min(d))