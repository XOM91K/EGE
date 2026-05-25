P = [d for d in range(5, 1000, 5)]
Q = [d for d in range(3, 1000, 3)]
mx = 1000
for A in range(mx, 1, -1):
    A2 = [d for d in range(A, 1000, A)]
    can = True
    for x in range(1, mx):
        if ((x in Q) <= ((x in P) <= ((x in Q) and (x in A2)))) == 0:
            can = False
    if can:
        print(A)
