s = open('18.txt').readline()
print(s)
ct = 1
mx = 0
for x in range(len(s) - 1):
    if not((s[x].isdigit() and s[x + 1].isdigit()) or (s[x].isalpha() and s[x + 1].isalpha())):
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx)