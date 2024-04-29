import re
s = open(r'C:\Users\Zarif\Downloads\24_demo (3).txt').readline()
m = re.findall(r"(?:XYZ)+(?:X|XY)?", s)
print(len(max(m, key=len)))