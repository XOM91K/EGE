for Q in range(-100,100):
    count=0
    d=[(3, 4, 1),(-2, -3, -1),(5, 12, 0),(0, 0, 0),
    (6, 8, 2),(-1, 2, -3),(7, 24, 5),(1, 1, 1),(9, 12, 3),(4, 3, -2),(10, 10, 10)]
    for m,n,p in d:
        if not((m ** 2 + n ** 2 > Q and p != 0) or (m + n + p< 0)):
            count+=1
    if count==5:
        print(Q)