s = open('19.txt').readline()
s = s.split('T')
mx = 0
for x in range(len(s) - 100):
    ct = 0
    for j in range(0, 101):
        ct += len(s[x + j])
    mx = max(mx, ct + 100)
print(mx)