import re
s = open(r'C:\Users\Zarif\Desktop\24var011.txt').readline()
s = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
m = re.findall(r'(?=(S(?:[^S1]*1){35}[^S1]*))', s)
print(max(m, key=len))
print(len(max(m, key=len)))
