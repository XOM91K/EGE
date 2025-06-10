import re
s = open(r'C:\Users\Zarif\Downloads\24_13866 (3).txt').readline()
for x in '13579':
    s = s.replace(x, '#')
s = s.split('###')
print(len(max(s, key=len)) + 4)
# m = re.findall(r'(?:\w*#{0,2})+\w*', s)
# print(len(max(m, key=len)) + 4)