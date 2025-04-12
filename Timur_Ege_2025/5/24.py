def v7(a):
    s = ''
    while a> 0:
        s += str(a % 7)
        a //= 7
    return s[::-1]
ct = 0
for N in range(343,2402):
    R = v7(N)
    if int(R[-1]) % 2 == 0:
        R = '6' + R
    else:
        R = '5' + R
    R = int(R,7)
    if R > 14500:
        ct += 1
print(ct)