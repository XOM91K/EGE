l = []
def f(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    if s == '':
        return '0'
    return s[::-1]
for N in range(1, 10000):
    R = f(N)
    if N % 2 == 0:
        R = R + f(3 * int(R[-1]))
    else:
        R = R[-1] + R[1:-1] + R[0] + '1'
    R = str(int(R))
    if R.count('0') == 4:
        l.append(N)
print(min(l))