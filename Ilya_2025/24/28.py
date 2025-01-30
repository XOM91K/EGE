import re
s = open(r'C:\Users\Zarif\Downloads\511_1 (2).txt').readline()
m = re.findall(r'(?:(?:0|[1-9]\d*)[+*])+(?:0|[1-9]\d*)', s)
for x in m:
    if eval(x) == 0:
        if len(x) > 100:
            print(len(x), x)
#print(eval('2+2*2'))
#asdihasdoRRsiadhsadshdoa