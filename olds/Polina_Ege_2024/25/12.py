for x in range(2023, 10 ** 8 + 1, 2023):
    d = str(x)
    if d[:2] == '11' and d[-2:] == '11':
        if int(d[2]) % 2 == 0 and int(d[-3]) % 2 != 0:
            print(x, x // 2023)