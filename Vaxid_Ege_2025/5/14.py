def v7(d):
    s = ''
    while d > 0:
        s += str(d % 7)
        d //= 7
    return s[::-1]
ct = 0
for N in range(343, 2402):
    R = v7(N)
    if R[-1] in '0246':
        R = '6' + R
    else:
        R = '5' + R
    R = int(R, 7)
    if R > 14500:
        print(N)
        ct += 1
print(ct)