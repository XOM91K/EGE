import string, re
s = open('8.txt').readline().replace('AHAHA', '#')
m = re.findall('\w+', s)
print(len(max(m, key=len)), max(m, key=len))