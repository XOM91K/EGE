s = open('18.txt').readline()
alf = []
for x in s:
    if x not in '0123456789ABCDEFGHI':
        alf.append(x)
        s = s.replace(x, '#')
    if len(set(alf)) == 26 - len('ABCDEFGHI'):
        break
s = s.split('#')
mx = 0
dd = ''
for x in s:
    if len(x) > 0 and x[0] != '0':
            if int(x, 19) > mx and int(x, 19) % 2 == 0:
                mx = int(x, 19)
                dd = x
print(dd)