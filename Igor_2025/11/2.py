import math
I = 126
I_o = 80 * 1024
for n in range(1, 100000):
    if (math.ceil((I + len(bin(n)[2:])) / 8) + 60) * n <= I_o:
        print(n)