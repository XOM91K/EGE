for xy in range(1000):
    for z in range(1000):
        if xy * 2 + z == 1000:
            if xy + z * 2 - xy * 3 == 200:
                print(z)