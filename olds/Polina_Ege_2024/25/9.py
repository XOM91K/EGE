import fnmatch
for x in range(42,2*10**8,42):
    if fnmatch.fnmatch(str(x),'?2*4*0'):
        if not(fnmatch.fnmatch(str(x),'1*7*')):
            print(x, x // 42)