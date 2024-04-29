import ipaddress
ct = 0
for x in ipaddress.ip_network("49.26.38.163/255.255.255.224", False).hosts():
    x = f'{x:b}'
    if x.count('1') % 2 != 0:
        ct += 1
print(ct)