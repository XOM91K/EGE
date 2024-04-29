s = open(r'C:\Users\Zarif\Downloads\24_11465.txt').readline()
s = s.replace('8', '9')
s = s.replace('B', 'A')
s = s.replace('C', 'A')
ct = 1
mx = 0
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
        mx = max(mx, ct)
    else:
        ct = 1
print(mx)