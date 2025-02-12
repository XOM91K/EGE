import re
s = open(r'C:\Users\Zarif\Desktop\24.txt').readline()
m = re.findall(r'A(?:[1-9]+\+)+[1-9]+', s)
print(max(m, key=len))
m = re.findall(r'A[1-9]+', s)
print(max(m, key=len))
print()