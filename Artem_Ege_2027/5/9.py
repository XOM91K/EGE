d = []
for N in range(1, 10000):
    R = bin(N)[2:]
    if sum(map(int, str(N))) % 2 != 0:
        R = R + '1'
    else:
        R = R + '0'
    N = int(R, 2)
    if sum(map(int, str(N))) % 2 != 0:
        R = R + '1'
    else:
        R = R + '0'
    N = int(R, 2)
    if sum(map(int, str(N))) != 0:
        R = R + '1'
    else:
        R = R + '0'
    R = int(R , 2)
    if R > 2064:
        d.append(R)
print(min(d))


# N = 1222854
# print(str(N).count('1') + str(N).count('2') * 2 + str(N).count('3') * 3 + str(N).count('4') * 4 + str(N).count('5') * 5 + str(N).count('6') * 6 + str(N).count('7') * 7 + str(N).count('8') * 8 + str(N).count('9') * 9)
# print(sum(map(int, str(N))))