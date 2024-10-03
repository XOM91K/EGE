P = list(range(16, 85))
Q = list(range(27, 44))
A = []
for x in range(1, 1000):
    if (((x in A) <= (x in P)) or (x in Q)) == 0:
        A.append(x)
print(A)