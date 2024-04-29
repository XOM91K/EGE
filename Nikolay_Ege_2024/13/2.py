import ipaddress
ct = 0
for x in ipaddress.ip_network('117.32.0.0/255.224.0.0', False):
    x = str(x).split('.')
    if len(set(x)) == 3:
        ct += 1
        print(x)
print(ct)