s = open(r'24_2024.txt').readline()
s = s.split('T')
k = 100
mx = 0
for x in range(len(s) - k):
    ct = 0
    for y in range(k + 1):
        ct += len(s[y + x])
    mx = max(mx, ct + k)
print(s)
