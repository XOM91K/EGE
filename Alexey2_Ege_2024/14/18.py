mx = 0
for x in range(14):
    for y in range(14):
        d1 = 7 *14 **4 + x *14 ** 3 + 3 *14 **2 + 7 *14 ** 1 + y
        d2 = 9 * x **3 + y * x ** 2 + 6 * x **1 + 3
        d3 = 1 * y **4 + 5 * y ** 3 + 1 *y ** 2 + 4 * y ** 1 + 8
        mx = max(mx, d1 + d2 - d3)
        if d1 + d2 - d3 == 325389:
            print(325389 // (x + y))
print(mx)