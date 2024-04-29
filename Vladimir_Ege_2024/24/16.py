s = open('16.txt').readline()
s = s.split('.')
mx = 0
for x in range(len(s) - 3):
    mx = max(mx, len(s[x] + s[x + 1] + s[x + 2] + s[x + 3]) + 3)
print(mx)