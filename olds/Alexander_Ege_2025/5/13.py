# https://examinf.ru/tasks/268
def v8(d):
    s = ''
    while d > 0:
        s += str(d % 8)
        d //= 8
    return s[::-1]
sm = 0
for N in range(10000, 100000):
    R = v8(N)
    for b in '1357':
        R =R.replace(b, "2")
    R += str(N % 8)
    R = int(R, 8)
    R = v8(R)
    for b in '1357':
        R = R.replace(b, "2")
    R += str(N % 8)
    R = int(R, 8)
    if R % 2023 == 0:
        sm += N
print(sm)