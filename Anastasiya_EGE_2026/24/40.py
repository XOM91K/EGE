import re
s = open(r'C:\Users\Zarif\Downloads\1483_1 (7).txt').readline()
s = s.replace('CDE', '#')
m = re.findall(r'(?:#[^#]*?){86}#[^#E]+?', s)
print(len(min(m, key=len)) + 2 * 87)
print(min(m, key=len))