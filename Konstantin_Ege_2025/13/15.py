import ipaddress
for x in ipaddress.ip_network('218.194.82.148/255.255.255.192', False):
    print(x)