import fnmatch, tqdm
for x in tqdm.tqdm(range(206, 10 ** 8, 206)):
    if fnmatch.fnmatch(str(x), '123*??56'):
        x = str(x)
        if x[-4] in '13579':
            if x[-3] in '02468':
                if int(x) % 206 == 0:
                    print(x, int(x) // 206)