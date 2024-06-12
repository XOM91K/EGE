import fnmatch
mx = 0
for x in range(1_000_001_268, 10_000_000_000, 2023):
    if fnmatch.fnmatch(str(x), '1*1'):
        if sum(map(int, str(x))) == 68:
            print(x, x // 2023)
#1999769891 988517
#1895989991 937217