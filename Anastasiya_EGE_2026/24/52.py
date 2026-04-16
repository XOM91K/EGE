import re
s = open(r'C:\Users\Zarif\Downloads\24_26077.txt').readline()
m = re.findall(r'G(?:[^G13579]*[13579]){45}[^G13579]*', s)
print(max(m, key=len))
print(len(max(m, key=len)))