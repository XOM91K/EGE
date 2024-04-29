s = open('3.txt').readline()
ct = 1
mx = 0
print(s)
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
        mx = max(mx, ct)
    else:
        ct = 1
print(mx)