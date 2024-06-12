s = open('35.txt').readline()
ct = 1
mx = 1
for x in range(len(s) - 1):
    if (s[x] in 'ABC' and s[x + 1] in 'ABC') or (s[x] in '6789' and s[x + 1] in '6789'):
        ct = 1
    else:
        ct += 1
        mx = max(mx, ct)
print(mx)
#'22 B1A1B1B1B1 11'