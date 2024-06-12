import fnmatch
for x in range(98591, 10 ** 11 + 1, 98591):
    if fnmatch.fnmatch(str(x), '123*452?1?'):
        print(x, x // 98591)