s = open(r'C:\Users\Zarif\Downloads\1397_2 (4).txt').readline()
s = s.split('RSQ')
mn = 10 ** 10
for i in range(len(s) - 128):
    ln = 0
    for j in range(0, 129):
        ln += len(s[i + j])
    mn = min(mn, ln + 3 * 130)
print(mn)