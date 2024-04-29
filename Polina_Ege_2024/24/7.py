import string
s = open(r'C:\Users\Zarif\Downloads\24_633_1 (1).txt').readline()
alf = string.ascii_uppercase
gl = 'AEIOUY'
sg = 'BCDFGHJKLMNPQRSTVWXZ'
for x in gl:
    s = s.replace(x, '@')
for x in sg:
    s = s.replace(x, '$')
s = s.replace('$$@', '*')
s = s.replace('$@@', '*')
print(s)