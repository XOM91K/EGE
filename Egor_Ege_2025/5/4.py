b = []
for N in range(10000, 100000):
    d = N
    for i in range(2):
        R = oct(d)[2:]
        R = R.replace("1", "2")
        R = R.replace("3", "2")
        R = R.replace("5", "2")
        R = R.replace("7", "2")
        R = R.replace("9", "2")
        R = R + str(N % 8)
        d = int(R, 8)
    if d % 2023 == 0:
        b.append(N)
print(sum(b))