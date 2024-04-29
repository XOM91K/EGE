import ipaddress
ct = 0
#тут метод hosts..
for x in ipaddress.ip_network('117.32.0.0/255.224.0.0', False).hosts():
    x = str(x).split('.')
    if len(set(x)) == 3:
        ct += 1
print(ct)




