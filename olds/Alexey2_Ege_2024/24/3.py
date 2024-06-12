s = open('3.txt').readline().split('.')
mx = 0
for x in range(len(s) - 2):
    mx = max(mx, len(s[x] + s[x + 1] + s[x + 2]) + 2)
print(s)