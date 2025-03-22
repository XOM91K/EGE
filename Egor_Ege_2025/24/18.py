s = open(r'C:\Users\Zarif\Downloads\1088_1 (3).txt').readline()
s = s.split('CD')
mx_ln = 0
for x in range(len(s) - 160):
    ln = 0
    for y in range(161):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln + 320 + 2)
print(mx_ln)