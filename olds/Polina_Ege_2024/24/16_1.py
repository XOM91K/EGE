s = open('16.txt').readline()
X = s.split('X')
Y = s.split('Y')
Z = s.split('Z')
mn_len = min([len(X), len(Y), len(Z)])
mx = 0
for x in range(mn_len - 5):
    ln1 = len(X[x] + X[x + 1] + X[x + 2] + X[x + 3] + X[x + 4] + X[x + 5])
    ln2 = len(Y[x] + Y[x + 1] + Y[x + 2] + Y[x + 3] + Y[x + 4] + Y[x + 5])
    ln3 = len(Z[x] + Z[x + 1] + Z[x + 2] + Z[x + 3] + Z[x + 4] + Z[x + 5])
    mx = max(mx, min([ln1, ln2, ln3]) + 15)
print(mx)
