import fnmatch
for x in range(2023, 10 ** 9, 2023):
    if fnmatch.fnmatch(str(x), '20*23'):
        sm_cif = sum(map(int, str(x)))
        if sm_cif % 7 == 0 and sm_cif < 20:
            print(x, x // 2023)
        # pattern - шаблон (маска
# 2023 1
# 204323 101
# 4444 10000
# 2025023 1001
# 20232023 10001
# 202302023 100001