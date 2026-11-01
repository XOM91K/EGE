import re
s = open('/Users/zarif/Downloads/154_1.txt').readline()
m = re.findall(r'(?:WXYZ|XYZ|YZ|Z)?(?:VWXYZ)+(?:VWXY|VWX|VW|V)?', s)
print(len(max(m, key=len)))