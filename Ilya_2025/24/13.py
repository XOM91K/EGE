s = open('13.txt').readline()
mx = 0
ct = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
        mx = max(mx, ct)
    else:
        ct = 1
print(mx)