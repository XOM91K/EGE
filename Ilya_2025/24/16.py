s = open('16.txt').readline()
print(s)
mx_len = 0
for x in range(len(s)):
    a = []
    for y in range(x, len(s)):
        a.append(s[y])
        if len(a) != len(set(a)):
            mx_len = max(mx_len, len(a) - 1)
            break
print(mx_len)