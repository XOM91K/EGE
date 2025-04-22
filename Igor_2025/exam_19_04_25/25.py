from fnmatch import fnmatch


for n in range(0, 10**10, 7993):
    s = str(n)
    fl = fnmatch(s, '4*4736*1')
    if fl:
        print(n, int(n/7993))