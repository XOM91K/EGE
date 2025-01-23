import re
s = open(r'154_1 (1).txt').readline()
m = re.findall(r'(?:Z|YZ|XYZ|WXYZ)?(?:VWXYZ)+(?:VW|V|VWX|VWXY)?', s)
print(len(max(m, key=len)))
print(max(m, key=len))