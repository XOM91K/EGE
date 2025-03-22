s = open(r'C:\Users\Zarif\Downloads\1062_1 (3).txt').readline()
s = s.split('FGSW')
mx_ln = 0
for x in range(len(s) - 85):
    ln = 0
    for y in range(86):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln + 4 * 85 + 6)
print(mx_ln)
