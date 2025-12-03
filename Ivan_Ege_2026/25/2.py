import fnmatch
for i in range(2023000, 10**10, 2023):
    if fnmatch.fnmatch(str(i), '1?1?1?1*1'):
        if sum(map(int, str(i))) == 22:
            print(i, i // 2023)
# a = '123123'
# print(sum(map(int, a)))