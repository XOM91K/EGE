import re
s = 'd1dh129d8+790025544322dhg89002554432289d1dg918g'
m = re.findall(r"\+7[0-9]{10}|8[0-9]{10}", s)
print(m)