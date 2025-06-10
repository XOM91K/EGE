import string
s = open('7.txt').readline()
for x in 'AEIOUY':
    s = s.replace(x, '#')
for x in string.ascii_uppercase:
    if x not in 'AEIOUY':
        s = s.replace(x, '@')
s = s.replace('@#@', '%')
s = s.split('%')
mx_ln = 0
for x in range(len(s) - 2):
    mx_ln = max(mx_ln, len(s[x] + s[x + 1] + s[x + 2]) + 6)
print(mx_ln)