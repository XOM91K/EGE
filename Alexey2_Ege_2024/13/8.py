import ipaddress
for x in ipaddress.ip_network('164.59.151.82/255.255.255.0', False):
    x = str(x).split('.')
    if int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) == 367:
        print(x)
    break