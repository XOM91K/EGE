for v in range(3, 100):
    w = "3" + v*"5"
    while '25' in w or '355' in w or '555' in w:
        if '25' in w:
            w = w.replace('25','32',1)
        if '355' in w:
            w = w.replace('355', '25',1)
        if '555' in w:
            w = w.replace('555','3',1)
    if w.count("2") == 5:
        print(v)