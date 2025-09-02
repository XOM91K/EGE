s = open(r'C:\Users\Zarif\Downloads\1088_1 (5).txt').readline()
s = s.split('CD')
mx = 0
for x in range(len(s) - 160):
    ln = 0
    for y in range(161):
        ln += len(s[x + y])
    mx = max(mx, ln + 160 * 2)
print(mx)