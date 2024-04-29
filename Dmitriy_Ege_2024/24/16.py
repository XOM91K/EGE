import re
s = open(r'C:\Users\Zarif\Downloads\24_625_1 (2).txt')
s = s.readline()
s = s.replace('FAT', '@').replace('BAD', '@').split('@')

mn_ln = 10 ** 10
for x in range(1, len(s) - 2):
    fb = 9
    ln = 0
    if s[x] == '':
        ln += 3
        fb -= 3
    if s[x + 1] == '':
        ln += 3
        fb -= 3
    if s[x] != '':
        ln += len(s[x])
    if s[x + 1] != '':
        ln += len(s[x + 1])
    mn_ln = min(mn_ln, ln + fb)
print(mn_ln)
print(s)
