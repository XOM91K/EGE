import re
s = open(r'C:\Users\Zarif\Downloads\1739_1.txt').readline()
m = re.findall(r'(?:\((?:[1-9]\d*[12346789]|1|2|3|4|6|7|8|9)[+-](?:[1-9]\d*[50]|5)\))+', s)
print(len(max(m, key=len)))