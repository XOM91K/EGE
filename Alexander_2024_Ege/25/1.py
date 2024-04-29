for n in range(2025, 10 ** 8, 2025):
    n = str(n)
    if n[:2] == '12' and n[-1] == '5' and n[-4:-2] == '34':
        print(int(n), int(n) // 2025)