s = open(r'C:\Users\Zarif\Downloads\1090_1 (4).txt').readline()
s = s.split('.')
mx = 0
for x in range(len(s) - 5):
    mx = max(mx, len(s[x] + s[x + 1] + s[x + 2] + s[x + 3] + s[x + 4] + s[x + 5]))
print(mx + 5)