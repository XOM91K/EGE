s = open(r'C:\Users\Zarif\Downloads\1266_1.txt').readline()
s = s.split('AB')
mx_ln = 0
for x in range(len(s) - 100):
    ln = 0
    for y in range(0, 101):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln)
print(mx_ln + 200 + 2)
