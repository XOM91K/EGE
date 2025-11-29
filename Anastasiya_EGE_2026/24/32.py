s = open(r'C:\Users\Zarif\Downloads\1088_1 (6).txt').readline()
s = s.split('CD')
mx_ln = []
for x in range(len(s) - 160):
    ln = 0
    for y in range(161):
        ln += len(s[x + y])
    mx_ln.append(ln)
print(max(mx_ln) + 160 * 2 +2 )