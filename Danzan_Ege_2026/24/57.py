import re
s = open(r'C:\Users\Zarif\Downloads\1487_1 (2).txt').readline()
m = re.findall(r'(?=([ABC][abc]*(?: [abc]+)*\.))', s)
print(max(m, key=len), len(max(m, key=len)))