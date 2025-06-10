import time
start = time.time()
s = open(r'C:\Users\Zarif\Downloads\1415_1.txt').readline()
r = []
ct = 0
mx = 10 ** 10
ans = 0
for i in range(len(s)):
    if s[i] != 'X':
        ct += 1
    else:
        r.append(ct)
        if s[i] == 'Y':
            r = []
        elif len(r) == 499:
            ans = sum(r)
        elif len(r) > 499:
            ans = ans + r[-1] - r[-500]
            mx = max(mx, ans)
        ct = 0
print(mx + 500)
finish = time.time()
print(finish - start)