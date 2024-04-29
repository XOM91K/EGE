import ipaddress
d = ipaddress.IPv4Network('49.26.38.163/255.255.255.224', False)
print(d)
ct = 0
for x in ipaddress.ip_network("49.26.38.160/255.255.255.224", False).hosts():
    x = f'{x:b}'
    if x[-1] == '1':
        ct += 1
print(ct)