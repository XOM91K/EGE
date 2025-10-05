import time
start = time.time()
for A in range(1, 10000):
    can = True
    for x in range(1, 10000):
        if (((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)) == 0:
            can = False
            break
    if can:
        print(A)
finish = time.time()
print(finish - start)