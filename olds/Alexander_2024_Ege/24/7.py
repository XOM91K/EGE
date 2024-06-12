import re
s = open(r'C:\Users\Zarif\Downloads\24_9791.txt').readline()
m = re.findall(r"[0-9a-fA-F]+", s)
print(len(max(m, key=len)))