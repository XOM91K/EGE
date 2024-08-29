for x in range(0, 36):
    s = '1' * x
    while '111' in s:
        s = s.replace('111', '33', 1)
        s = s.replace('333', '1', 1)
    if s == '131':
        print(x)