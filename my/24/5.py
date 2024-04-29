s = open(r'5.txt').readline()
flag = True
ct = 0
mx = 0
find = 'FSWY'
ind = 0
for x in range(len(s)):
    if s[x] in 'FSWY':
        sym = s[x]
        if flag:
            ind = find.index(s[x])
            flag = False
        if find[ind % 4] == s[x]:
            ct += 1
            ind += 1
        else:
            mx = max(mx, ct)
            ct = 0
            flag = True
    else:
        mx = max(mx, ct)
        ct = 0
        flag = True
print(mx)
