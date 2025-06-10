import re
s = open(r'C:\Users\Zarif\Downloads\24_19149 (2).txt').readline()
m = re.findall(r'\(((?:[1-4]+\+)+[1-4]+)\)', s)
mx_ln = 0
for x in m:
    if eval(x) % 2 == 0:
        mx_ln = max(mx_ln, len(x) + 2)
print(mx_ln)