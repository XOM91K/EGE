ct = 0
for A in range(300):
    k = 0
    for x in range(300):
        for y in range(300):
            if (((x < 5) <= (x ** 2 < A)) and ((y * y <= A) <= (y <= 5))) == 1:
                k += 1
    if k == 300 * 300:
        ct += 1
print(ct)