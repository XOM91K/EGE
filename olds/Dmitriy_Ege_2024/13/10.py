import ipaddress
ct = 0
for x in ipaddress.ip_network('112.154.132.0/255.255.252.0', False).hosts():
    x = f'{x:b}'
    if x[:16].count('1') <= x[-16:].count('0') and x[-16:].count('0') % 2 != 0:
        ct += 1
print(ct)