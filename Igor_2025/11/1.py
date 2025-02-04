cnt = 20 * 1024
import math
for i in range(1, 1000000):
    I = 95 + 40 * 8
    I += len(bin(i)[2:])
    I = math.ceil(I / 8)
    if (cnt - I) == 0:
        print(i)
        break
    elif (cnt - I) < 0:
        print(i - 1)
        break
    else:
        cnt -= I