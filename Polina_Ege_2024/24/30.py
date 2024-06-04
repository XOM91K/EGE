s = open(r'C:\Users\Zarif\Downloads\24 (23).txt').readline()
s = s.replace('E', 'A')
s = s.replace('O', 'A')
s = s.replace('U', 'A')
s = s.replace('L', 'K')
s = s.replace('M', 'K')
s = s.replace('N', 'K')
mx = 0
ct = 1
for x in range(len(s) - 1):
    if s[x] + s[x + 1] != 'AA' and s[x] + s[x + 1] != 'KK':
        ct += 1
        mx = max(mx, ct)
    else:
        ct = 1
print(mx)