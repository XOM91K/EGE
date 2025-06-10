import fnmatch
for x in range(6679, 10 ** 10, 6679):
    if fnmatch.fnmatch(str(x), '4*4736*1'):
        print(x, x // 6679)