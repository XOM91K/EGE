import ipaddress
ct = 0
for x in ipaddress.ip_network("102.12.21.201/255.255.252.0", False).hosts():
    x = f'{x:b}'
    if x.count('1') % 2 == 0:
        ct += 1
print(ct)