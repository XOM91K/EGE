def f(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]
for N in range(1, 10000):
    R = f(N)
    if len(R) % 2 == 0:
        R = R[:len(R) // 2] + '0' + R[len(R) // 2:]
    if int(R) <= 180:
        print(N)
# s = 'СОЛНЫШКО'
# s = s[:len(s) // 2] + '0' + s[len(s) // 2:]
# print(s)
# s = 'ГОРА'
# s = s[:len(s) // 2] + '0' + s[len(s) // 2:]
# print(s)