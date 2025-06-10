def v4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n //= 4
    return s[::-1]
for N in range(1, 10000):
    R = v4(N)
    if len(R) % 2 == 0:
        R = R[:len(R) // 2] + '0' + R[len(R) // 2:]
    if int(R) <= 180:
        print(N)

# s = '3333333333'
# s = s[:len(s) // 2] + '0' + s[len(s) // 2:]
# print(s)