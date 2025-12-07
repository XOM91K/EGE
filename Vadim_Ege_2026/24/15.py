import re
r = open(r"C:\Users\Zarif\Downloads\988_1 (6).txt").readline()
m = re.findall(r'(?:\.[A-Z]*){6}\.',r)
print(len(min(m,key=len)))