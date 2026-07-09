import re
s = open(r'C:\Users\Zarif\Downloads\24 (50).txt').readline()
m = re.findall(r'(?=(\d{12}))', s)
r = []
for x in m:
    if len(set(x)) <= 3:
        r.append(len(x))
print(max(r))