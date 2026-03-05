for p in range(10, 100):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    if len(set([x, y, z, w])) == 4:
                        c1 = y*p**3 + 0*p**2 + 7*p**1 + x*p**0
                        c2 = w*p**3 + y*p**2 + 9*p**1 + z*p**0
                        c3 = z*p**4 + x*p**3 + y*p**2 + x*p**1 + y*p**0
                        if c1 + c2 == c3:
                            print(x * p ** 3 + y * p ** 2 + z * p + w)