def v7(d):
    s = ''
    while d > 0:
        s = str(d % 7) + s
        d //= 7
    return s
ct = 0
for N in range(343, 2402):
    R = v7(N)
    if R[-1] == '4' or R[-1] == '0' or R[-1] == '2' or R[-1] == '6':
        R = '6' + R
    else:
        R = '5' + R
    R = int(R,7)
    if R > 14500:
        ct += 1
print(ct)