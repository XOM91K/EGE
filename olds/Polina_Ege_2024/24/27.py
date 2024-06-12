s = open(r'C:\Users\Zarif\Downloads\24 (18).txt').readline()
s = s.split('E')
mn_ln = 10 ** 10
print(s[:20])
for x in range(len(s) - 238):
    ln = 0
    for y in range(0, 239):
        ln += len(s[x + y])
    mn_ln = min(mn_ln, ln + 240)
print(mn_ln)