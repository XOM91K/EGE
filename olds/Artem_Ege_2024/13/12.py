import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.160.0/255.255.224.0', False):
    x = f'{x:b}'
    if x.count('1') == 19:
        ct += 1
print(ct)