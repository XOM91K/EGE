# def v8(N):
#     s = ''
#     while N > 0:
#         s += str(N % 8)
#         N //= 8
#     return s[::-1]
for N in range(11, 10000):
    R = oct(N)[2:]
    if N % 5 == 0:
        R = R + R[:3]
    else:
        R = R + bin(N % 5)[2:]
    R = int(R, 8)
    if R >= 35000:
        print(N)