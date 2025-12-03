for x in range(2024, 10 ** 10, 2024):
        s = str(x)
        if s[0] == '3' and s[2:6] == '2258' and s[-1] == '4':
            print(x)