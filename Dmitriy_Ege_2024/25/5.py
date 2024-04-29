import fnmatch
for x in range(79, 10 ** 8, 100):
    if fnmatch.fnmatch(str(x), '124*5*79'):
        if x % sum([int(d) for d in str(x) if int(d) % 2 != 0]) == 0:
            print(x, sum([int(d) for d in str(x)]))