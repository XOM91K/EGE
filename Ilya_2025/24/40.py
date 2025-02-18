# import re
# s = open(r'C:\Users\Zarif\Downloads\988_1.txt').readline()
# m = re.findall(r'', s)
import re
a = open(r'C:\Users\Zarif\Downloads\988_1.txt').readline()
m = re.findall(r'(?:\.\w*?){6}\.',a)
print(len(min(m, key=len)))
a = a.split('.')
minn=10**6
for i in range(len(a)-5):
    minn = min(minn,len(a[i])+len(a[i+1])+len(a[i+2])+len(a[i+3])+len(a[i+4])+len(a[i+5]))
print(minn + 7)