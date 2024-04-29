import ipaddress
for x in ipaddress.ip_network('164.59.151.82/255.255.248.0',False):
    #x = bin(int(x))[2:]
    x = str(x).split('.')
    if int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) == 367:
        print(x)