import string
print(string.ascii_uppercase)
s = open('14.txt').readlines()
mx_rast = 0
for x in s:
    x = x.strip()
    mx_rast = 0
    if x.count('A') < 25:
        for y in string.ascii_uppercase:
            mx_rast = max(mx_rast, x.rfind(y) - x.find(y))
        print(mx_rast)