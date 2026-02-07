import fnmatch

for i in range(10980, 10 ** 10, 10980):
    if fnmatch.fnmatch(str(i), '20??22*'):
        if int(str(i)[2]) % 2 == int(str(i)[3]) % 2 == 1:
            if len(str(i)) == 6:
                print(i, i // 10980)
            else:
                a = str(i)[6:]
                c = 0
                for e in a:
                    if int(e) % 2 == 0:
                        c += 1
                if c == len(a):
                    print(i, i // 10980)
