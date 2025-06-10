import re
s = open(r'C:\Users\Zarif\Downloads\24_5832.txt').readline()
m = re.findall(r'9?8?7?6?5?4?3?2?1?0?', s)
print(max(m, key=len))