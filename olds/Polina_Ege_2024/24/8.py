import string
s = open(r'C:\Users\Zarif\Downloads\24_619_1 (3).txt').readlines()
alp = string.ascii_uppercase
ct = 0
for y in s:
    for x in alp:
        if 'Z' + x + 'RO' in y:
            ct += 1
            break

print(ct)