for n in range(3, 10000):
    s = "2" + "7" * n
    while "27" in s or "777" in s or "377" in s:
        if "27" in s:
            s = s.replace("27", "7", 1)
        if "777" in s:
            s = s.replace("777", "3", 1)
        if "377" in s:
            s = s.replace("377", "72", 1)
    pr = 1
    for y in s:
        pr *= int(y)
    if pr % 3 == 0 and str(pr)[-1] == "1":
        print(n)
