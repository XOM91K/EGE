import re
s = open(r'C:\Users\Zarif\Downloads\24_7043 (1).txt').readline()
m = re.findall(r'0\w*?1\w*?2\w*?3\w*?4\w*?5\w*?6\w*?7\w*?8\w*?9\w*?a\w*?b\w*?c\w*?d\w*?e\w*?f', s)
print(len(min(m, key=len)))