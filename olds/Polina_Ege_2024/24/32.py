s= open(r'32.txt').readline()
s = s.split('F')
mx = 0
count = 0

for i in range(len(s)):
    if s[i].count('A') <= 2:
        count += len(s[i])+1
        mx = max(mx, count)
    else:
        count = 0
print(mx + 1)