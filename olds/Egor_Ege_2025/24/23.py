import re
s = open(r'C:\Users\Zarif\Downloads\328_1 (4).txt').readline()
s= s.split('CD')
mx = 0
for x in range(len(s) - 50):
    ln = 0
    for y in range(0, 51):
        ln += len(s[x + y])
    mx = max(mx, ln + 100 + 2)
print(mx)