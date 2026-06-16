import re
s = open(r'C:\Users\Zarif\Downloads\24 (40).txt').readline()
m = re.findall(r'D\w*?C\w*?B\w*?A\w*?9\w*?8\w*?7\w*?6\w*?5\w*?4\w*?3\w*?2\w*?1\w*?0', s)
print(len(min(m,key=len)))