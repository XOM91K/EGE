s = open(r'C:\Users\Zarif\Downloads\1062_1 (10).txt').readline()
s = s.split('FGSW')
mx = []
for x in range(len(s) - 85):
    ln = 0
    for y in range(0, 86):
        ln += len(s[x + y])
    mx.append(ln)
print(max(mx) + 6 + (4 * 85))