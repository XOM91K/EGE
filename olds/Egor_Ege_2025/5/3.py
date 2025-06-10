def v4(a):
    s = ""
    while a > 0:
        s += str(a%4)
        a //= 4
    return s[::-1]

mx = 0
for N in range(1, 100000):
    R = v4(N)
    if len(R) % 2 == 0:
        R = R[:len(R) // 2] + '0' + R[len(R) // 2:]
    if int(R) <= 180:
        mx = max(mx, N)
print(mx)