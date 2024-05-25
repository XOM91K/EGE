s = open(r'29.txt').readline()
dl = []
s = s.replace('A', '@')
s = s.replace('E', '@')
s = s.replace('U', '@')
s = s.replace('B', '#')
s = s.replace('C', '#')
s = s.replace('D', '#')
s = s.replace('F', '#')
s = s.split('#@#')
for x in range(len(s) - 2):
    dl.append(len(s[x]) + len(s[x + 1]) + len(s[x + 2]) + 6)
print(max(dl))