import re
s = open('17.txt').readline()
print(s)
mx_len = 0
for x in range(len(s)):
    a = []
    for y in range(x, len(s)):
        a.append(s[y])
        if a.count('F') == 2:
            mx_len = max(mx_len, len(a) - 1)
            break
print(mx_len)