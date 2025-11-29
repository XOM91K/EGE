for x in range(0, 10000):
    if '8' not in str(x) and '9' not in str(x):
        if int(str(x), 8) + int('20', 4) * int('25', 16) == int('2025', 8):
            print(x)