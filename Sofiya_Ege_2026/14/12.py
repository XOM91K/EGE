for p in range(10, 37):
    for x in range(0, p):
        for y in range(1, p):
            for z in range(1, p):
                for w in range(1, p):
                   if len(set([x, y, z, w])) == 4:
                       # a=int(f'{y}07{x}', p)
                       # b=int(f'{w}{y}9{z}', p)
                       # c=int(f'{z}{x}{y}{x}{y}', p)
                       a = y * p ** 3 + 7 * p + x
                       b = w * p ** 3 + y * p ** 2 + 9 * p + z
                       c = z * p ** 4 + x * p ** 3 + y * p ** 2 + x * p + y
                       if a+b==c:
                           print(p, x * p ** 3 + y * p ** 2 + z * p + w)