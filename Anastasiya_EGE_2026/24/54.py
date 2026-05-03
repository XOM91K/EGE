s = open(r'C:\Users\Zarif\Downloads\24_29354.txt').readline()
s = s.split('BC')
mx_ln = []
for x in range(len(s) - 190):
    ln = 0
    for y in range(191):
        ln += len(s[x + y])
    mx_ln.append(ln)
print(max(mx_ln) + 2 * 190 + 2)