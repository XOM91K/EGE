s = open(r'C:\Users\Zarif\Downloads\1088_1 (7).txt').readline()
s = s.split('CD')
mx = []
for x in range(len(s) - 160):
    ln = 0
    for y in range(0, 161):
        ln += len(s[x + y])
    mx.append(ln)
print(max(mx) + 160 * 2)