for n in range(1, 1000):
    s = ">2" + n * "12" + "<"
    while ">2<" not in s:
        s = s.replace(">1", ">2", 1)
        s = s.replace(">21", "1>", 1)
        s = s.replace("12<", "1<2", 1)
        s = s.replace("1<", "<2", 1)
    h = s.count("1")+ s.count("2") * 2
    if h > 103:
        print(n)