#C:\Users\Zarif\Downloads\1172_1.txt
import re
a = open(r'C:\Users\Zarif\Downloads\1172_1.txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*)[+*])+(?:[1-9]\d*)', a)
mx_chisla = 0
for x in m:
    d = x
    x = x.replace('+', '*')
    x = x.split('*')
    mx_chisla = max(mx_chisla, len(x))
    if len(x) == 52:
        print(d)
        print(x)
        print(len(x))
        break
print(mx_chisla)