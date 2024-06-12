import string
s = open('3.txt').readlines()
ct = 0
for x in s:
    for y in string.ascii_uppercase:
        if 'Z' + y + 'RO' in x:
            ct += 1
            break
print(ct)