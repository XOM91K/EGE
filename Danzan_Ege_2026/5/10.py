def v3(d):
    s = ''
    while d > 0:
        s += str(d%3)
        d //= 3
    return s[::-1]

mn = []
for N in range(11, 1000):
    chet = 0
    nechet = 0
    R = v3(N)
    for i in range(len(R)):
        if int(R[i])%2 == 0:
            chet += 1
        if int(R[i])%2 != 0:
            nechet += 1
    if chet > nechet:
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        mn.append(R)
print(min(mn))