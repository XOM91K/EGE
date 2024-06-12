#6651
s = open('25.txt').readline()
s = s.replace('BAD', '@').replace('FAT', '@')
s = s.split('@')
mn = 10 ** 10
for x in range(len(s) - 1):
    mn = min(mn, len(s[x] + s[x + 1]) + 9)
print(mn)