#7 23
for x in range(10000, 100000):
    s1 = int(str(x)[0]) + int(str(x)[2]) + int(str(x)[4])
    s2 = int(str(x)[1]) + int(str(x)[3])
    if min(s1, s2) == 7 and max(s1, s2) == 23:
        print(x)