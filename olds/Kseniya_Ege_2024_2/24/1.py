s = open('1.txt').readline()
s = s.replace('A', '@')
s = s.replace('B', '@')
s = s.replace('C', '@')
s = s.replace('6', '#')
s = s.replace('7', '#')
s = s.replace('8', '#')
s = s.replace('9', '#')
mx = 0
ct = 1
print(s)
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx)