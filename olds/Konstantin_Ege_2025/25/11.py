import fnmatch
for x in range(206, 10**8, 206):
    if fnmatch.fnmatch(str(x), '123*??56'):
        if str(x)[-4] in '13579':
            if str(x)[-3] in '02468':
                print(x, x // 206)