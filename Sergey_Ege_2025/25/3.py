import fnmatch
for x in range(98591, 10 ** 10, 98591):
        if fnmatch.fnmatch(str(x), '5?2*3?3?'):
            print(x, x // 98591)