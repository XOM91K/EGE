import re
t=open(r'C:\Users\Zarif\Downloads\24-204.txt').readline()
t = t.replace('AA', '#').replace('CC', '#')
print(t)
# c = 1
# while '#' * c in t:
#     print(c)
#     c += 1
m=re.findall(r'(?:AA|CC){1310}', t)
print(len(max(m, key=len)))
print(max(m, key=len))

# t=open('1').readline()
# reg=r'(AA|CC)+'
# ren=rf'(?=({reg}))'
# m=max((x.group(1) for x in finditer(ren, t)), key=len)
# print(len(m)//2)