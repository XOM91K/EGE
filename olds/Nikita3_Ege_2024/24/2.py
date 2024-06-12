import string
#print(string.ascii_uppercase)
s = open('2.txt').readline()
for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    s = s.replace(x, '@')
s = s.split('@')
mn = 10 ** 10
for x in s:
    if len(x) > 0 and int(x) % 2 == 0:
        mn = min(mn, int(x))
print(mn)