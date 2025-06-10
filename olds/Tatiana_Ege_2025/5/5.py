# 34722223
# 45138887
for N in range(45138888, 45138888 + 1):
    R = bin(N)[2:]
    R += bin(N % 3)[2:].zfill(2)
    R += bin(N % 5)[2:].zfill(3)
    R = int(R, 2)
    print(N, R)