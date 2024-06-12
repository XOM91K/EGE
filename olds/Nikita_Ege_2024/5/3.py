for N in range(3001):
    r = bin(N)[2:]
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    if int(r, 2) > 150:
        print(int(r, 2))