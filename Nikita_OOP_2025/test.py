import re
string = 'P1(-30,20) P2(-10,-10) P3(-20,-30)'
m = re.findall(r'\((-?\d+),(-?\d+)\)', string)
print(m)