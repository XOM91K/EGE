s = open(r'C:\Users\Zarif\Downloads\988_1 (4).txt').readline()
s = s.split('.')
mn_ln = []
for x in range(len(s) - 5):
    mn_ln.append(len(s[x] + s[x + 1] + s[x + 2] + s[x + 3] + s[x + 4] + s[x + 5]))
print(min(mn_ln) + 7)