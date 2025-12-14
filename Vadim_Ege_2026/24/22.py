import re
l = open(r"C:\Users\Zarif\Downloads\327_1 (8).txt").readline()
m = re.findall(r'[A-Z]([1-9][0-9]*[02468])[A-Z]',l)
#m = [int(x) for x in m if int(x)%2==0]
print(max(m, key=int))
#7642289