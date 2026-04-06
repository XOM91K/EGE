import math
for N in range(1, 10001):
    P = math.prod((map(int, str(N).replace('0', '1'))))
    M = int(max(str(N))) + int(min(str(N)))
    T1 = P + M
    T2 = P * M
    #print(T1, T2, str(min(T1,T2))+str(max(T1,T2)))
    if int(str(min(T1,T2))+str(max(T1,T2))) == 23126:
        print(N)