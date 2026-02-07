import re
s = open(r'C:\Users\Zarif\Downloads\1266_1 (5).txt').readline()
s = s.split('AB')
mx_ln = []
for x in range(len(s) - 100):
    ln = 0
    for y in range(0, 101):
        ln += len(s[x + y])
    mx_ln.append(ln + 200)
print(max(mx_ln))