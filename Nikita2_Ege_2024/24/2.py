s = open('3.txt').readline()
for x in '02468ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    s = s.replace(x, '#')
s = s.split('#')
print(max(s, key=len))