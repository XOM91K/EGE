import fnmatch
l = [x.strip() for x in open('14.txt')]
s = set()
for x in l:
    if fnmatch.fnmatch(x, '195.2*.?*.14'):
        print(x)
        s.add(x)
print(len(s))