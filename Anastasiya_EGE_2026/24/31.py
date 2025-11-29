# import re
# m=open(r'C:\Users\Zarif\Downloads\1090_1 (5).txt').readline()
# s=re.findall(r'\w+(?:\w*.){5}\w+', m)
# print(len(max(s ,key=len)))
s=open(r'C:\Users\Zarif\Downloads\1090_1 (5).txt').readline()
s = s.split('.')
mx_ln = []
for x in range(len(s) - 5):
    mx_ln.append(len(s[x])+len(s[x + 1])+len(s[x + 2])+len(s[x + 3])+len(s[x + 4])+len(s[x + 5]))
print(max(mx_ln) + 5)