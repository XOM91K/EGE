s = open(r'C:\Users\Zarif\Desktop\ЕГКР\3 Вар\24.txt').readline()
s = s.split('FSR')
mx_ln = 0
for x in range(len(s) - 79):
    ln = 0
    for y in range(0, 80):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln + 80 * 3 + 2)
print(mx_ln)
# FSRAAAAAAFSRAAAAAAFSRAAAAAAAAAAAAAAAAAAAAAAFSRAAAAAAFSRAAAAAAFSRAAAAAAFSRAAAAAA
# две FSR