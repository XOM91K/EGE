for x in range(2023, 10 ** 10, 2023):
    if str(x)[0] == '1' and str(x)[-1] == '4' and str(x)[2:6] == '2139':
        print(x, x // 2023)