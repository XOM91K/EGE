s = open('11.txt').readline()
mx = 0
ct = 1
r = s[0]
for x in range(len(s) - 1):
    if s[x] > s[x + 1]:
        ct += 1
        r += s[x + 1]
    else:
        mx = max(mx, ct)
        if mx == 6:
            print(r)
            break
        r = s[x + 1]
        ct = 1
print(mx)

