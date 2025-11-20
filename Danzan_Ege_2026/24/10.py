s = open(r'C:\Users\Zarif\Downloads\391_1 (7).txt').readline()
# s = s.split('AXMM')
# print(max(s, key=len))
# print(len(max(s, key=len)) + 6)
mx = []
ln = 0
for x in range(len(s) - 3):
    if s[x] + s[x + 1] + s[x + 2] + s[x + 3] == 'AXMM':
        mx.append(ln)
        ln = 0
    else:
        ln += 1
print(max(mx) + 3)