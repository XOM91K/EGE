import re, string
#print(string.ascii_uppercase)
s = open(r'C:\Users\Zarif\Downloads\24_162_1.txt').readline()
m = re.findall(r"(?<=Y)(?:[A-XZ]*Y){150}[A-XZ]*(?=Y)", s)
print(max(m, key=len))
print(len(max(m, key=len)))