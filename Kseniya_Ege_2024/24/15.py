s = open('15.txt').readline()
s = s.split('A')
mx = 0
for i in range(len(s) - 2):
    if s[i].count('B') + s[i + 1].count('B') + s[i + 2].count('B') <= 2:
        mx = max(mx, len(s[i] + s[i + 1] + s[i + 2]) + 2)
print(mx)
s = open('15.txt').readline()
s = s.split('B')
for i in range(len(s) - 2):
    if s[i].count('A') + s[i + 1].count('A') + s[i + 2].count('A') <= 2:
        mx = max(mx, len(s[i] + s[i + 1] + s[i + 2]) + 2)
print(mx)