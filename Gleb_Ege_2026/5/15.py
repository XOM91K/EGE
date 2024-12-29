l = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if sum(map(int, str(N))) % 2 == 1:
        R = R + '1'
    else:
        R = R + '0'
    N = int(R, 2)
    if sum(map(int, str(N))) % 2 == 1:
        R = R + '1'
    else:
        R = R + '0'
    N = int(R, 2)
    if sum(map(int, str(N))) % 2 == 1:
        R = R + '1'
    else:
        R = R + '0'
    R = int(R, 2)
    if R > 2064:
        l.append(R)
print(min(l))