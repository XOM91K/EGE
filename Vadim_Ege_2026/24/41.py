import re
l = open(r'C:\Users\Zarif\Downloads\1266_1 (6).txt').readline()
l = l.split('AB')
mx_ln = []
for x in range(len(l) - 100):
    ln = 0
    for y in range(0, 101):
        ln += len(l[x + y])
    mx_ln.append(ln + 2 * 100 + 2)
print(max(mx_ln))
# l = l.replace('AB', 'XZ')
# m = re.findall(r'(?=(Z?(?:[^XZ]*XZ){100}[^XZ]*X?))',l)
# print(max(m,key=len))
# print(len((max(m,key=len))))