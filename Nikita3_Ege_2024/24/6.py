s = open('6.txt').readline()
s = s.split('KEGE')
mx = 0
print(s)
for x in range(len(s) - 2):
    mx = max(mx, len(s[x]) + len(s[x + 1]) + len(s[x + 2]) + 8)
print(mx + 6)