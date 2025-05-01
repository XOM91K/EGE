import time
start = time.time()
s = open(r'C:\Users\Zarif\Downloads\1414_1.txt').readline()
#s = open('21.txt').readline()
r = []
ct = 0
mx = 0
ans = 0
for i in range(len(s)):
    if s[i] != 'T':
        ct += 1
    else:
        r.append(ct)
        if len(r) == 101:
            ans = sum(r)
        elif len(r) > 101:
            ans = ans + r[-1] - r[-102]
            mx = max(mx, ans)
        ct = 0
print(mx + 100)
print(len('AAAATAAAAAAAAAAAAAAAATAAAA'))
finish = time.time()
print(finish - start)