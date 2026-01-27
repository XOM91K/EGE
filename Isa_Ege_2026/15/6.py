for A in range(1, 20000):
    k=0
    for x in range(1,20001):
            if (not((x % 263 == 0) <= (x % A == 0)) and (x % 71 == 0)) == False:
                k+=1
            else:
                break
    if k==20000:
        print(A)