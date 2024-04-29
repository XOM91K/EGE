import ipaddress
ct=  0
for x in ipaddress.ip_network("98.162.71.94/255.255.255.0", False):
    print(x)
    ct += 1
print(ct)