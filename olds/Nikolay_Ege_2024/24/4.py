s = open('4.txt').readline()
ct = 0
mx = 0
for x in s:
    if x not in 'CF':
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 0
print(mx)