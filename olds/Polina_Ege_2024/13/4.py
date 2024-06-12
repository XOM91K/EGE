import ipaddress
ct = 0
for x in ipaddress.ip_network('140.19.96.0/255.255.248.0'):
    d = f'{x:b}'
    if d[:8].count('1') == d[8:16].count('1') == d[16:24].count('1') == d[24:32].count('1'):
        ct += 1
print(ct)