import ipaddress
ct = 0
for x in ipaddress.ip_network("90.65.32.0/255.255.224.0", False):
    x = f'{x:b}'
    if x.count('1') == x.count('0'):
        ct += 1
print(ct)