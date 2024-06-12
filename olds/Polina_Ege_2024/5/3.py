for N in range(1, 10000):
    R = hex(N)[2:]
    if N % 2 == 0:
        R += sorted(R)[-1]
    else:
        R += '0'
    for k in range(2):
        s = 0
        for x in R:
            if x.isdigit():
                s += int(x)
            else:
                s += ord(x) - 87
        R += str(s % 16)
    if R.count(sorted(R)[-1]) / R.count(sorted(R)[0]) == 5:
        print(N, int(R, 16))
        break