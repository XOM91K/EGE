s = open('9.txt').readline()
s = s.replace('J', '#')
s = s.replace('O', '#')
s = s.split('#')
s2 = []
for x in s:
    if s[0] != '0':
        s2.append(x)
print(len(max(s2, key=len)))