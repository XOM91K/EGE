import re
s = open(r'C:\Users\Zarif\Downloads\24_19149 (1).txt').readline()
m = re.findall(r'\((?:\d+\+)+\d+\)', s)
mx_ln = 0
for x in m:
    if eval(x[1:-1]) % 2 == 0:
        mx_ln = max(mx_ln, len(x))
print(mx_ln)
# print(max(m, key=lambda d: (len, eval(d) % 2 == 0)))
# print(len(max(m, key=lambda d: (len, eval(d) % 2 == 0))))
