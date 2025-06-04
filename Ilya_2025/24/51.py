import re
a = open(r'C:\Users\Zarif\Downloads\1513_1.txt').readline()
#m = re.findall(r'(?<![0-9+])([1-9]\d{2}(?:[+*][1-9]\d{2})+)',a)
m = re.findall(r'(?:[1-9]\d{2}[+*])+[1-9]\d{2}',a)
print(len(max(m,key=len)))