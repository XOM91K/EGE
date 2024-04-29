s = open('26.txt').readline()
s = s.replace('A', '@')
s = s.replace('B', '@')
s = s.replace('C', '@')
s = s.replace('6', '#')
s = s.replace('7', '#')
s = s.replace('8', '#')
s = s.replace('9', '#')
print(s)
mx = 0
ct = 1
for x in range(len(s) - 1):
    if s[x] + s[x + 1] not in '@@' and s[x] + s[x + 1] not in '##':
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx)