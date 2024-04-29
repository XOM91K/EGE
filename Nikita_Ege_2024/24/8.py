import string
s = open(r'C:\Users\Zarif\Downloads\24_619_1.txt').readlines()
alf = string.ascii_uppercase
ct = 0
for x in s:
    for y in alf:
        if 'Z' + y + 'RO' in x:
            ct += 1
            break
print(ct)