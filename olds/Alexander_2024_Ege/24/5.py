s = open(r'C:\Users\Zarif\Downloads\24_9753 (2).txt').readline()
ln = [0] * 151
ct = 0
mx_ln = 0
for x in s:
    if x != 'Y':
        ct += 1
    else:
        ln.append(ct)
        mx_ln = max(mx_ln, sum(ln[-151:]) + 150)
        ct = 0
print(mx_ln)