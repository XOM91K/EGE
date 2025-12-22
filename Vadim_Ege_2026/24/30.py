import re
s = open(r'C:\Users\Zarif\Downloads\24_21421 (2).txt').readline()
m = re.findall(r'[1-9AB][0-9AB]+[02468A]', s)
print(len(max(m, key=len)))
print(max(m, key=len))
# 503450920023089B5009999999ASDASDAS