import string
s = open(r'C:\Users\Zarif\Downloads\24_322.txt').readline()
for x in '0123456789':
    s = s.replace(x, '#')
for x in string.ascii_uppercase:
    s = s.replace(x, '@')
print(s.count('#@@@@#'))