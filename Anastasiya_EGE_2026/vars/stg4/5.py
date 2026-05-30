import math
for N in range(1, 10000):
    N = 234
    P = math.prod([int(x) for x in str(N) if int(x) > 0])
    M = int(max(str(N))) + int(min(str(N)))
    T1 = P + M
    T2 = P * M
    R = int(str(min(T1, T2)) + str(max(T1, T2)))
    print(R)
    break
    if R == 23126:
        print(N)