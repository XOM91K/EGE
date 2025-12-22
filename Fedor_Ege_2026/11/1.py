import math
for N in range(1, 10000):
    id = 4783 * 1024 * 8 / 21980
    if math.ceil(id / 405) < math.log2(N):
        print(N)
        break