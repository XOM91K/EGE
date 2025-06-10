s = open(r'C:\Users\Zarif\Downloads\24_19489 (2).txt').readline()
mx_ln = 0
for i in range(len(s) - 1):
    for j in range(i + mx_ln, len(s)):
        if s[i:j].count('WWF') <= 120 and s[i:j].count('WSFWW') == 0:
            mx_ln = max(mx_ln, j - i)
        else:
            break
print(mx_ln)