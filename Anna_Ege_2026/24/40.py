import re
s = open(r'C:\Users\Zarif\Downloads\24 (37).txt').readline()
m = re.findall(r'\d+', s)
mx_ln = []
for x in m:
    if len(set(x)) <= 3:
        mx_ln.append(len(x))
print(max(mx_ln))