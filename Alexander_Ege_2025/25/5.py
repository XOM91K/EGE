for x in range(206, 10 ** 8, 206):
    s = str(x)
    if s[:3] == '123' and s[-2:] == '56' and s[-4] in '13579' and s[-3] in '02468':
        print(x, x // 206)