l = open(r'C:\Users\Zarif\Downloads\1554_1.txt').readline()
for x in 'abcdefghijklmnopqrstuvwxyz':
    l = l.replace(x, '#')
l = l.split('#')
print(l)
print(len(max(l, key = len)))
