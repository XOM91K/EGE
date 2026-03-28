n = 36000
for a in range(n, 1, -1):
    k = 0
    for x in range(1, n + 1):
        if ((x % 465 == 0) <= ((x % a != 0) <= (x % 385 != 0))) == True:
            k+=1
        else:
            break
    if k==n:
        print(a)
        break