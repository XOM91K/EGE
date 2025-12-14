s = open(r'C:\Users\Zarif\Downloads\1022_1 (1).txt').readline()
s = s.split('FSRQ')
mx = []
for x in range(len(s) - 80):
    ln = 0
    st = ''
    for y in range(0, 81):
        st += s[x + y] + 'FSRQ'
        ln += len(s[x + y])
    if ln == 2053:
        print(st)
    mx.append(ln)
print(max(mx) + 80 * 4 + 6)
print(max(mx))