for x in range(100, 1000):
    s1 = (x // 100) + (x // 10 % 10)
    s2 = (x // 10 % 10) + (x % 10)
    if min(s1, s2) == 12 and max(s1, s2) == 14:
        print(x)