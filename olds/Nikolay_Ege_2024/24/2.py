import string
s = open(r'C:\Users\Zarif\Downloads\24-1.txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x, '@')
s = s.split('@')
for x in s:
    if len(x) > 0 and x != '\n' and int(x) % 2 != 0:
        print(x)