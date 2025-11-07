d = []
def v3(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]
for N in range(1, 10000):
    R = v3(N)
    if R[0] == '3':
        R = R.replace('1', '*')
        R = R.replace('3', '1')
        R = R.replace('*', '3')
        R = '21' + R
    else:
        R = '1' + R[1:] + '12'
    R = int(R, 4)
    if R == 597:
        print(N)
        d.append(R)
print(max(d))