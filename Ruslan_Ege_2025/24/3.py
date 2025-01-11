s = open(r'C:\Users\Zarif\Downloads\174_1 (2).txt').readline()
mx_len = 0
for i in range(1, 26):
    for x in range(len(s) - i - 1):
        if len(set(s[x:x + i])) == i:
            mx_len = i
print(mx_len)