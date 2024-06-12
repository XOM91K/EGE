k = 1
mx = 0
s = open(r'23.txt').readline()
for n in range(1, len(s)):
    if s[n - 1] != s[n]:
        k += 1
    else:
        mx = max(mx, k)
        k = 1
print(mx)