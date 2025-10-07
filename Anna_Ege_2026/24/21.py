import string
s = open(r'C:\Users\Zarif\Downloads\196_1 (8).txt').readline()
for x in string.ascii_uppercase: #AA A A
    s = s.replace(x + x, x + ' ' + x)
s = s.split()
print(len(max(s, key=len)))