for n in range(1, 50):
    l = ">" + 17 * "0" + n * "3" + 17 * "2"
    while ">3" in l or ">2" in l or ">0" in l:
        if ">3" in l:
            l = l.replace(">3", "22>", 1)
        if ">2" in l:
            l = l.replace(">2", "2>", 1)
        if ">0" in l:
            l = l.replace(">0", "3>", 1)
    if ((3 * l.count("3") + 2 * l.count("2")) ** 0.5) % 1 == 0:
        print(n, 3 * l.count("3") + 2 * l.count("2") )