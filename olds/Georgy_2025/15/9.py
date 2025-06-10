import time
start = time.time()
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((9 * x + y > A) or (x >= 36) or (y >= 18)) == 0:
                can = False
    if can:
        print(A)
finish = time.time()
print(finish - start)