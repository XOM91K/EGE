from collections import Counter
s = open(r'C:\Users\Zarif\Downloads\24 (3).txt').readline()
s_ans = ''
for x in range(len(s) - 2):
    if s[x] == s[x + 2]:
        s_ans += s[x + 1]
print(Counter(s_ans))