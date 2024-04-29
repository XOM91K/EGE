s = open('5.txt').readline()
s = s.split('.')
mn = 10 ** 10
for x in range(len(s) - 5):
    mn = min(mn, len(s[x] + s[x + 1] + s[x + 2] + s[x + 3] + s[x + 4] + s[x + 5]))
print(mn+7)