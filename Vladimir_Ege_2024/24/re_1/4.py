import re
s = '<table width="100%" border="0" width= "85%" scale="1" width=    "50%">'
m = re.findall("width\s*=\s*\"(\d{1,3})%\"", s)
print(m)