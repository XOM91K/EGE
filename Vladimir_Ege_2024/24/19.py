s = open('19.txt').readline()
mx = 0
ct = 1
for x in range(len(s) - 1):
    if ord(s[x]) < ord(s[x + 1]):
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx)