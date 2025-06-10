s = open(r'C:\Users\Zarif\Downloads\24_6734 (1).txt').readline()
s = s.split('.')
mn = 10 ** 10
for x in range(len(s) - 5):
    ln = 0
    for y in range(0, 6):
        ln += len(s[x + y])
    mn = min(mn, ln + 7)
print(mn)