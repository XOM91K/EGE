mx = []
for N in range(1000,10000):
    R = oct(N)[2:]
    R = R.replace("0", "1", 1)
    R = R.replace("2", "1", 1)
    R = R.replace("4", "1", 1)
    R = R.replace("6", "1", 1)
    R = str(R) + str(N % 8)
    R = int(R,8)
    N = R
    R = oct(R)[2:]
    R = R.replace("0", "1", 1)
    R = R.replace("2", "1", 1)
    R = R.replace("4", "1", 1)
    R = R.replace("6", "1", 1)
    R = str(R) + str(N % 8)
    R = int(R, 8)
    if R%234==0:
        mx.append(R)
print(max(mx))