P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
A = []
ct = 0
for x in range(1000):
    if (((x in A) <= (x in P)) and ((x not in Q) <= (x not in A))) == 0:
        A.append(x)