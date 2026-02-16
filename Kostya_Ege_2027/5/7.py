for N in range(100, 1000):
    s = str(N)
    sm1 = int(s[0]) + int(s[1])
    sm2 = int(s[1]) + int(s[2])
    if str(max(sm1, sm2)) + str(min(sm1, sm2)) == '1715':
        print(N)