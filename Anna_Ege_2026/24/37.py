import re
s = open(r'C:\Users\Zarif\Downloads\1721_1 (1).txt').readline()
m = re.findall(r'G(?:[^G13579]*[13579]){45}[^G13579]*', s)
print(len(max(m, key = len)))