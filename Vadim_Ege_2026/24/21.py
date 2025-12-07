s = open(r'C:\Users\Zarif\Downloads\24_23281 (1).txt').readline()
s = s.split('Y')
mx = []
for x in range(len(s) - 80):
    ln = 0
    ct = 0
    for y in range(0, 81):
        ct += s[x + y].count('2025')
        ln += len(s[x + y])
    if ct >= 90:
        mx.append(ln)
print(max(mx) + 80)