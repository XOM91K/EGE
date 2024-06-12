import string
s = open('10.txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x, '#')
for x in string.digits:
    s = s.replace(x, '@')
s = s.replace('#@@', '%')
s = len('%%%%%%%%%%%%%%%%%%%')
print(s * 3)