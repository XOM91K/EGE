import ipaddress
ct = 0
for x in ipaddress.ip_network('192.168.160.0/255.255.224.0', False).hosts():
    x = f'{x:b}'
    m = f"{ipaddress.ip_address('255.255.224.0'):b}"
    if x.count('1') == m.count('1'):
        ct += 1
print(ct)