for x in range(1000, 10000):
    s = str(x)
    pr1 = int(s[0]) * int(s[1])
    pr2 = int(s[2]) * int(s[3])
    if min(pr1, pr2) == 12 and max(pr1, pr2) == 14:
        print(x)