for x in range(10980, 10 ** 10, 10980):
    s = str(x)
    if s[:2] == '20' and s[4:6] == '22':
        if s[2] in '13579' and s[3] in '13579':
            if '1' not in s[6:] and '3' not in s[6:] and '5' not in s[6:] and '7' not in s[6:] and '9' not in s[6:]:
                print(x, x // 10980)