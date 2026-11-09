for x in range(2024, 10 ** 10 + 1, 2024):
    x = str(x)
    if x[0:3] == "112" and x[4:6] == "57" and x[-1] == "4" and sum(map(int, str(x))) % 2 != 0:
        print(x, int(x) // 2024)