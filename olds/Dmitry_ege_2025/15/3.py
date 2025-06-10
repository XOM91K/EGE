import time
start = time.time()
for A in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x >= 27) or (2 * x < 3 * y) or (A > (x + 2) * (y - 3))) == 0:
                can = False
                break
        if can == False:
            break
    if can == True:
        finish = time.time()
        print(A, finish - start)
#18.549657344818115
#18.549657344818115
#0.8239681720733643