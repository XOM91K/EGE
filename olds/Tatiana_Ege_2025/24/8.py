import string
s = open(r'C:\Users\Zarif\Downloads\327_1 (2).txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x, '*')
s = s.split('*')
mx_chet = 0
for x in s:
    if len(x) > 1:
        if int(x) % 2 == 0:
           mx_chet = max(mx_chet, int(x))
print(mx_chet)