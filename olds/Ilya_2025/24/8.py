s = open('8.txt').readline()
ct = 1
mx = 1
for x in range(len(s) - 1):
    if not((s[x].isalpha() and s[x + 1].isalpha()) or (s[x].isdigit() and s[x + 1].isdigit())):
        ct += 1
        mx = max(mx, ct)
    else:
        ct = 1
print(mx)