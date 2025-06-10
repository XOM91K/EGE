import re
s = open(r'C:\Users\Zarif\Downloads\154_1.txt').readline()
match = re.findall(r"(?:VWXYZ)+(?:V|VW|VWX|VWXY)?", s)
print(max(match, key=len))
print(len(max(match, key=len)))