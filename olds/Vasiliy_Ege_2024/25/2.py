for x in range(9573, 10 ** 10 + 1, 9573):
    x = str(x)
    if x[:3] == '202' and x[-1] == '6' and '47' in x[3:-1]:
        print(x, int(x) // 9573)