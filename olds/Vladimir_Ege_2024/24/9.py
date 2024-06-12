import string
print(string.ascii_uppercase)
s = open('9.txt').readline()
for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': #на * заменить
    s = s.replace(x, '*')
s = s.split('*')
for x in s:
    if len(x) != 0 and int(x) % 2 != 0:
        print(x)