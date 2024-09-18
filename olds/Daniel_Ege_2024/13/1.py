import ipaddress
for x in ipaddress.ip_network("98.162.71.94/98.162.71.64", False):
    print(x)