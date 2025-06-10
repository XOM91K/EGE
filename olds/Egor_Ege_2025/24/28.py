import re
s = open(r'C:\Users\Zarif\Downloads\1487_1.txt').readline()
m = re.findall(r'[ABC] ?(?:[abc]+ )+[abc]+\.', s)
print(len(max(m, key=len)))
print(max(m, key=len))
