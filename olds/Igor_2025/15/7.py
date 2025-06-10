r = []
for A in range(1, 400):
    can = True
    for x in range(1, 400):
        for y in range(1, 400):
            if ((x - 3 * y < A) or (y > 400) or (x > 56)) == 0:
                can = False
                break
        if can == False:
            break
    if can:
        r.append(A)
print(min(r))