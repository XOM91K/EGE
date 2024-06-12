ct = 0
for x in range(1000,10000):
    R = str(x)
    if int(R[0]) % 4 == 0:
        R = '9' + R[1:]
    if int(R[0]) % 2 == 0 and int(R[0]) % 4 != 0:
        R = '3' + R[1:]
    if R[0] == '9' and oct(int(R))[-1] == '4':
        ct += 1
print(ct)