s = open(r'C:\Users\Zarif\Downloads\24-181.txt').readline()
s = s.split('.')
mx = 0
for x in range(len(s) - 1):
    mx = max(mx, len(s[x]) + len(s[x + 1]) + 1)
print(mx)