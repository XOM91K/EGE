ct = 0
for N in range(1000, 10000):
    N = str(N)
    if int(N[0]) % 4 == 0:
        N = '9' + N[1:]
    if int(N[0]) % 2 == 0 and int(N[0]) % 4 != 0:
        N = '3' + N[1:]
    if N[0] == '9' and oct(int(N))[-1] == '4':
        ct += 1
print(ct)