s = open('20.txt').readline()
s = s.replace('Y', 'X')
s = s.split('X')
mx = 0
for x in range(len(s) - 5):
    mx = max(mx, len(s[x]) + len(s[x + 1]) + len(s[x + 2]) + len(s[x + 3]) + len(s[x + 4]) + + len(s[x + 5]) + 5)
print(mx)