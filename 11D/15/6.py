mx = 0
for A in range(1000):
    can = False
    for x in range(1000):
        for y in range(1000):
            if ((4 *x + y > 115) or (x > 3 * y) or (x + 4 * y < A)) == 0:
                mx = max(mx, A)
                print(mx)
                can = True
                break
        if can:
            break

print(mx)
