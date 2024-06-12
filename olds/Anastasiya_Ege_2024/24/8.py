import string
alf = 'GHIJKLMNOPQRSTUVWXYZ'
s = open('8.txt').readline()
for x in alf:
    s = s.replace(x, '?')
s = s.split('?')
print(len(max(s, key=len)))