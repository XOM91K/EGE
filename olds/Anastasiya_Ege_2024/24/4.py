import string
s = open('4.txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x, '(')
s = s.split('(')
mn = 10 ** 10
for x in s:
    if len(x) > 0:
        if int(x) % 2 == 0:
            mn = min(mn, int(x))
print(mn)