import re
s = open('154_1 (4).txt').readline()
m = re.findall(r'(?:WXYZ|XYZ|YZ|Z)(?:VWXYZ)+(?:VWXY|VWX|VW|V)', s)
print(len(max(m, key=len)))