g = []
for N in range(1, 10000):
    R = bin(N)[2:]
    R = R.replace('1', '#')
    R = R.replace('0', '1')
    R = R.replace('#', '0')
    R += str(R.count('1') % 2)
    R = int(R, 2)
    if R < 170:
        g.append(R)
print(max(g))