import fnmatch
for x in range(466963, 10**11, 466963):
    if fnmatch.fnmatch(str(x), "?9?38*6?"):
        if x % 2 == 0:
            print(x, x//466963)