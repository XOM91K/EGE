s = open(r'C:\Users\Zarif\Downloads\2_24.txt').readline()
find = 'FSWY'
ind = 0
flag = True
ct = 0
mx = 0
for x in range(len(s)):
    if s[x] in 'FSWY':
        if flag:
            ind = find.index(s[x])
            flag = False
        if find[ind % 4] == s[x]:
            ind += 1
            ct += 1
            mx = max(mx, ct)
        else:
            flag = True
            mx = max(mx, ct)
            ct = 0
    else:
        flag = True
        mx = max(mx, ct)
        ct = 0
print(mx)
