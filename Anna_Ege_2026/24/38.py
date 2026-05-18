import re
s = open(r'C:\Users\Zarif\Downloads\1565_1 (7).txt').readline()
# s = s.replace('BAC', '#')
# s = s.replace('CAB', '@')
m = re.findall(r'(?=((?:BAC|CAB)+))', s)
print(max(m, key = len))
print(len(max(m, key = len)))
#CABCABCABBAcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcab