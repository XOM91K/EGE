s = open(r'C:\Users\Zarif\Downloads\1062_1 (6).txt').readline()
s = s.split('FGSW')
mx_ln = []
for x in range(len(s) - 85):
    ln = 0
    for y in range(0, 86):
        ln += len(s[x + y])
    mx_ln.append(ln)
print(max(mx_ln) + 85 * 4 + 6)