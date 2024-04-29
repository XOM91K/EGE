ct = 0
import string
d = open(r'24_618_1.txt').readlines()
alf = string.ascii_uppercase
for s in d:
    for y in alf:
        if 'A' + y + 'R' in s:
            ct += 1
            break
print(ct)
