import fnmatch
s = open('1617.txt').readlines()
ct = 0
for x in s:
    x = x.strip()
    if fnmatch.fnmatch(x, '*Q*W*E*R*T*Y*'):
        print(x)
        ct += 1
print(ct)