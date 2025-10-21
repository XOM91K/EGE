def v9(n):
    s = ''
    while n > 0:
        s = str(n % 9) + s
        n //= 9
    return s
for N in range(1, 10000):
    R = v9(N)
    for y in range(5):
        if R.count('5') == R.count('7'):
            R += R[-1]
        else:
            cif = [0] * 9 # R = 14151
            for x in R:
                cif[int(x)] += 1
            mx = max(cif)
            for x in range(len(cif) - 1, -1, -1):
                if mx == cif[x]:
                    R += str(x)
                    break
    R = hex(int(R, 9))[2:]
    if 'bac' in R:
        print(N)

