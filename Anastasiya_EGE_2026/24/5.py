import string
s = open(r'C:\Users\Zarif\Downloads\24_318.txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x, '#')
s = s.split('#')
mx = 0
for x in s:
    if x != '' and x != '\n' and int(x) % 2 != 0:
        mx = max(mx, int(x))
print(mx)