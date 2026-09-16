def v8(d):
    s = ''
    while d > 0:
        s += str(d % 8)
        d //= 8
    return s[::-1]
sm = []
for N in range(10_000,100_000):
    R = v8(N)
    R = R.replace('1','2')
    R = R.replace('3','2')
    R = R.replace('5','2')
    R = R.replace('7','2')
    R += str(N % 8)
    R = int(R,8)
    R = v8(R)
    R = R.replace('1','2')
    R = R.replace('3','2')
    R = R.replace('5','2')
    R = R.replace('7','2')
    R += str(N % 8)
    R = int(R,8)
    if R % 2023 == 0:
        sm.append(N)
print(sum(sm))