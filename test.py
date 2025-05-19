for i in range(201455, 201471):
    d = []
    for x in range(1, i+1):
        if i % x == 0:
            d.append(x)
    if len(d) == 4:
        print(*sorted(d))