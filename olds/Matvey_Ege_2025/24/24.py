s = open(r'C:\Users\Zarif\Downloads\1266_1 (2).txt').readline()
s = s.split('AB')
mx = 0
for x in range(len(s) - 100):
    ln = 0
    for y in range(101):
        ln += len(s[x + y])
    mx = max(mx, ln + 2 * 100 + 2)
print(mx)