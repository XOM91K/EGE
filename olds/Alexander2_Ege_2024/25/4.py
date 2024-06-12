ct = 0
for x in range(320401, 1000_000):
    flag = True
    for y in range(10, 19, 2):
        if x % y != 0:
            flag = False
    if flag == True:
        print(x, x // 18)
        ct += 1
    if ct == 5:
        break